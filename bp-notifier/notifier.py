from collections import namedtuple
from concurrent.futures import Future, ThreadPoolExecutor

import datetime
import logging
import sys
import time

from core.constants import (
    DATE_FORMAT, DOC_TYPE, MAX_WORKERS, NOTE_FIELDS_COUNT, SPLIT_BY, START_DATE, TIMEOUT, WARN_NOTIFICATION_DAYS
)
from core.models import AppConfig, InvoiceItem
from core.request import ArchiveRequest, DocInvoiceRequest

InvoiceNoteInfo = namedtuple('InvoiceNoteInfo', ['num', 'name', 'phone', 'date_to'])

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
    name, phone, date_to = parse_note_fields(invoice.note)[:3]
    return InvoiceNoteInfo(invoice.num, name, phone, datetime.datetime.strptime(date_to, DATE_FORMAT).date())


def parse_note_fields(note) -> tuple[str, ...]:
    return tuple(map(str.strip, note.split(SPLIT_BY)))


def sort_invoices(invoice_notes: list[tuple[int, str, str, datetime.date]]):
    return sorted(invoice_notes, key=lambda note: (note[-1], note[0]))


def print_invoice_report(invoice_notes: list[InvoiceNoteInfo]):
    print()
    print(f'Отчет за {datetime.date.today().strftime(DATE_FORMAT)}')
    print()
    print(f'Общее количество: {len(invoice_notes)}')
    print()
    for note in sort_invoices(invoice_notes):
        num, name, phone, date_to = note
        now = datetime.date.today()
        days_diff = (date_to - now).days
        print(f'{'Договор #':<15s}: {num}')
        print(f'{'Имя':<15s}: {name}')
        print(f'{'Контакт':<15s}: {phone}')
        print(f'{'Действует до':<15s}: {date_to.strftime(DATE_FORMAT)}')
        print(f'{'Осталось дней':<15s}: {days_diff}{' (Просрочено)' if days_diff < 0 else ''}')
        print()


def main(config: AppConfig):
    try:
        api_key, db, firm = config.model_dump().values()

        archive_req = ArchiveRequest(api_key, db, firm)
        items = archive_req.get_full_doc_type_archive(DOC_TYPE, START_DATE)
        item_id_list = [item.object for item in items]
        logging.info(f'total: {len(item_id_list)}, items={item_id_list}')

        invoice_req = DocInvoiceRequest(api_key, db, firm)
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            tasks: list[Future] = [executor.submit(invoice_req.get_item, invoice) for invoice in item_id_list]

        invoices = [task.result(TIMEOUT) for task in tasks]

        invoice_notes = [
            extract_invoice_fields(invoice)
            for invoice in invoices
            if should_include_invoice(invoice.note)
        ]
        logging.info(f'{invoice_notes=}')

        print_invoice_report(invoice_notes)
    except Exception as ex:
        logging.error(f'Exception: {ex}')


if __name__ == '__main__':
    app_config = AppConfig()
    print(app_config)

    start_time = time.perf_counter()
    main(app_config)
    print(f"Done in {time.perf_counter() - start_time:.2f}s")
