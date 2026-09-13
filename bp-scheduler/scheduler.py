import datetime
import logging
import os
import sys

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


def filter_invoices(note: str) -> bool:
    if not note:
        return False

    split_note = split_notes(note)
    if len(split_note) != NOTE_FIELDS_COUNT:
        return False

    now = datetime.date.today()
    note_date = datetime.datetime.strptime(split_note[-1], DATE_FORMAT).date()
    days_diff = note_date - now
    if WARN_NOTIFICATION_DAYS and days_diff > datetime.timedelta(WARN_NOTIFICATION_DAYS):
        return False

    return True


def map_invoices(invoice: InvoiceItem):
    name, phone, date = split_notes(invoice.note)
    return invoice.num, name, phone, date


def split_notes(note) -> tuple[str, ...]:
    split_note = tuple(map(str.strip, note.split(SPLIT_BY)))
    return split_note


def sort_notes(invoice_notes: list[tuple[int, str, str, str]]):
    sort_by_date_to_invoice_num = lambda note: (note[-1], note[0])
    return sorted(invoice_notes, key=sort_by_date_to_invoice_num)


def format_output(invoice_notes: list[tuple[int, str, str, str]]):
    print()
    for note in sort_notes(invoice_notes):
        num, name, phone, date = note
        print(f'{'Договор #':<15s}: {num}')
        print(f'{'Имя':<15s}: {name}')
        print(f'{'Контакт':<15s}: {phone}')
        print(f'{'Действует до':<15s}: {date}')
        print()


def scheduler():
    archive_req = ArchiveRequest(api_key, db, firm)
    items = archive_req.get_full_doc_type_archive(DOC_TYPE, START_DATE)
    item_id_list = list(map(lambda item: item.object, items))
    logging.info(f'total: {len(item_id_list)}, items={item_id_list}')

    invoice_req = DocInvoiceRequest(api_key, db, firm)
    invoices = [invoice_req.get_item(invoice) for invoice in item_id_list]
    filtered_invoices = filter(lambda invoice: filter_invoices(invoice.note), invoices)
    invoice_notes = list(map(map_invoices, filtered_invoices))
    logging.info(f'{invoice_notes=}')

    format_output(invoice_notes)


if __name__ == '__main__':
    load_dotenv('.env')
    api_key, db, firm = os.getenv('API_KEY'), os.getenv('DB'), os.getenv('FIRM')
    logging.info(f'{api_key=}, {db=}, {firm=}')
    scheduler()
