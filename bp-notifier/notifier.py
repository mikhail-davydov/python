from collections import namedtuple
from concurrent.futures import Future, ThreadPoolExecutor

import logging
import sys
import time
from datetime import date, datetime

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

    now = date.today()
    note_date = datetime.strptime(split_note[-1], DATE_FORMAT).date()
    days_diff = (note_date - now).days

    # Если WARN_NOTIFICATION_DAYS = 0 или None, пропускаем проверку (показываем всё)
    if WARN_NOTIFICATION_DAYS:
        return days_diff <= WARN_NOTIFICATION_DAYS

    return True


def extract_invoice_fields(invoice: InvoiceItem):
    parts = parse_note_fields(invoice.note)
    if len(parts) < 3:
        logging.warning(f"Некорректный формат note для {invoice.num}: {invoice.note}")
        return None  # Возвращаем None, чтобы отфильтровать дальше

    name, phone, date_to = parts[:3]
    return InvoiceNoteInfo(invoice.num, name, phone, datetime.strptime(date_to, DATE_FORMAT).date())


def parse_note_fields(note: str) -> tuple[str, ...]:
    return tuple(map(str.strip, note.split(SPLIT_BY)))


def sort_invoices(invoice_notes: list[tuple[int, str, str, date]]):
    return sorted(invoice_notes, key=lambda note: (note[-1], note[0]))


def print_invoice_report(invoice_notes: list[InvoiceNoteInfo]):
    now = date.today()
    print()
    print(f'Отчет за {now.strftime(DATE_FORMAT)}')
    print()
    print(f'Общее количество: {len(invoice_notes)}')
    print()
    for note in sort_invoices(invoice_notes):
        num, name, phone, date_to = note
        days_diff = (date_to - now).days
        print(f'{'Договор #':<15s}: {num}')
        print(f'{'Имя':<15s}: {name}')
        print(f'{'Контакт':<15s}: {phone}')
        print(f'{'Действует до':<15s}: {date_to.strftime(DATE_FORMAT)}')
        print(f'{'Осталось дней':<15s}: {days_diff}{' (Просрочено)' if days_diff < 0 else ''}')
        print()


def main(config: AppConfig):
    try:
        api_key = config.api_key
        db = config.db
        firm = config.firm

        archive_req = ArchiveRequest(api_key, db, firm)
        items = archive_req.get_full_doc_type_archive(DOC_TYPE, START_DATE)
        item_id_list = [item.object for item in items]
        logging.info(f'total: {len(item_id_list)}, items={item_id_list}')

        max_workers = MAX_WORKERS or len(item_id_list)
        invoice_req = DocInvoiceRequest(api_key, db, firm)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            tasks: list[Future] = [executor.submit(invoice_req.get_item, invoice) for invoice in item_id_list]
            invoices = [task.result(TIMEOUT) for task in tasks]

        invoice_notes = [
            note for note in (
                extract_invoice_fields(invoice)
                for invoice in invoices
                if should_include_invoice(invoice.note)
            )
            if note is not None
        ]
        logging.info(f'{invoice_notes=}')

        print_invoice_report(invoice_notes)
    except Exception as ex:
        logging.error(f'Exception: {ex}', exc_info=True)
        raise


if __name__ == '__main__':
    app_config = AppConfig()
    print(app_config)

    start_time = time.perf_counter()
    main(app_config)
    print(f"Done in {time.perf_counter() - start_time:.2f}s")
