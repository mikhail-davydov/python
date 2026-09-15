import datetime
import logging
import os
import sys
import time

# from dotenv import load_dotenv
# from dotenv_vault import load_dotenv
from dotenvx import load_dotenv

from core.constants import NOTE_FIELDS_COUNT, DATE_FORMAT, WARN_NOTIFICATION_DAYS, SPLIT_BY, DOC_TYPE, START_DATE
from core.models import InvoiceItem
from core.request import ArchiveRequest, DocInvoiceRequest

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(module)s | %(message)s',
)


def should_include_invoice(note: str) -> bool:
    if not note:
        return False

    split_note = parse_note_fields(note)
    if len(split_note) < NOTE_FIELDS_COUNT:
        return False

    now = datetime.date.today()
    note_date = datetime.datetime.strptime(split_note[-1], DATE_FORMAT).date()
    days_diff = note_date - now
    if WARN_NOTIFICATION_DAYS and days_diff > datetime.timedelta(WARN_NOTIFICATION_DAYS):
        return False

    return True


def extract_invoice_fields(invoice: InvoiceItem):
    name, phone, date = parse_note_fields(invoice.note)[:3]
    return invoice.num, name, phone, date


def parse_note_fields(note) -> tuple[str, ...]:
    return tuple(map(str.strip, note.split(SPLIT_BY)))


def sort_invoices(invoice_notes: list[tuple[int, str, str, str]]):
    return sorted(invoice_notes, key=lambda note: (note[-1], note[0]))


def print_invoice_report(invoice_notes: list[tuple[int, str, str, str]]):
    print()
    print(f'Отчет за {datetime.date.today()}')
    print()
    print(f'Общее количество: {len(invoice_notes)}')
    print()
    for note in sort_invoices(invoice_notes):
        num, name, phone, date = note
        print(f'{'Договор #':<15s}: {num}')
        print(f'{'Имя':<15s}: {name}')
        print(f'{'Контакт':<15s}: {phone}')
        print(f'{'Действует до':<15s}: {date}')
        print()


def main():
    api_key, db, firm = os.getenv('API_KEY'), os.getenv('DB'), os.getenv('FIRM')

    archive_req = ArchiveRequest(api_key, db, firm)
    items = archive_req.get_full_doc_type_archive(DOC_TYPE, START_DATE)
    item_id_list = [item.object for item in items]
    logging.info(f'total: {len(item_id_list)}, items={item_id_list}')

    invoice_req = DocInvoiceRequest(api_key, db, firm)
    invoices = [invoice_req.get_item(invoice) for invoice in item_id_list]
    invoice_notes = [
        extract_invoice_fields(invoice)
        for invoice in invoices
        if should_include_invoice(invoice.note)
    ]
    logging.info(f'{invoice_notes=}')

    print_invoice_report(invoice_notes)


if __name__ == '__main__':
    load_dotenv('.env')
    start_time = time.perf_counter()
    main()
    print(f"Done in {time.perf_counter() - start_time:.2f} s")
