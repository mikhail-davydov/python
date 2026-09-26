from concurrent.futures import Future, ThreadPoolExecutor

import logging
import sys
import time
from datetime import date, datetime

from core.constants import (
    DATE_FORMAT, DOC_TYPE, MAX_WORKERS, NOTE_FIELDS_COUNT, SPLIT_BY, START_DATE, TIMEOUT, WARN_NOTIFICATION_DAYS
)
from core.models import AppConfig, InvoiceItem, InvoiceNoteInfo
from core.request import ArchiveRequest, DocInvoiceRequest

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(module)s | %(message)s',
)


def should_include_invoice(date_to: date) -> bool:
    now = date.today()
    days_diff = (date_to - now).days

    # Если WARN_NOTIFICATION_DAYS = 0 или None, пропускаем проверку (показываем всё)
    if WARN_NOTIFICATION_DAYS:
        return days_diff <= WARN_NOTIFICATION_DAYS

    return True


def extract_invoice_fields(invoice: InvoiceItem) -> InvoiceNoteInfo:
    try:
        note = invoice.note
        if not note:
            logging.warning(f'Отсутствует note для {invoice.num}')
            return InvoiceNoteInfo(invoice.num, None, None, None, error='Отсутствует note')

        parts = tuple(map(str.strip, invoice.note.split(SPLIT_BY)))
        if len(parts) < NOTE_FIELDS_COUNT:
            logging.warning(f'Некорректный формат note для договора #{invoice.num}: {invoice.note}')
            return InvoiceNoteInfo(invoice.num, None, None, None, error=f'Некорректный формат {invoice.note=}')

        name, phone, date_to = parts[:NOTE_FIELDS_COUNT]
        return InvoiceNoteInfo(invoice.num, name, phone, datetime.strptime(date_to, DATE_FORMAT).date(), error=None)
    except Exception as ex:
        logging.error(f'Ошибка при извлечении данных из invoice.note: {ex}', exc_info=True)
        return InvoiceNoteInfo(invoice.num, None, None, None, error=ex)


by_date_and_num = lambda note: (note.date_to, note.num)
by_num = lambda note: note.num


def print_invoice_report(invoice_notes: list[InvoiceNoteInfo], invalid_invoice_notes: list[InvoiceNoteInfo]):
    now = date.today()
    print()
    print(f'Отчет за {now.strftime(DATE_FORMAT)}\n')
    print(f'Общее количество: {len(invoice_notes)}\n')
    for note in sorted(invoice_notes, key=by_date_and_num):
        num, name, phone, date_to, _ = note
        days_diff = (date_to - now).days
        print(f'{'Договор #':<15s}: {num}')
        print(f'{'Имя':<15s}: {name}')
        print(f'{'Контакт':<15s}: {phone}')
        print(f'{'Действует до':<15s}: {date_to.strftime(DATE_FORMAT)}')
        print(f'{'Осталось дней':<15s}: {days_diff}{' (Просрочено)' if days_diff < 0 else ''}\n')

    print(f'Ошибок: {len(invalid_invoice_notes)}\n')
    for note in sorted(invalid_invoice_notes, key=by_num):
        num, *_, error = note
        print(f'Договор # {num}: {error}')


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

        all_invoice_notes = list(map(extract_invoice_fields, invoices))

        valid_invoice_notes: list[InvoiceNoteInfo] = []
        invalid_invoice_notes: list[InvoiceNoteInfo] = []
        [
            valid_invoice_notes.append(invoice) if not invoice.error
            else invalid_invoice_notes.append(invoice)
            for invoice in all_invoice_notes
        ]

        invoice_notes = [
            invoice_note
            for invoice_note in valid_invoice_notes
            if should_include_invoice(invoice_note.date_to)
        ]
        logging.info(f'{invoice_notes=}')

        print_invoice_report(invoice_notes, invalid_invoice_notes)
    except Exception as ex:
        logging.error(f'Exception: {ex}', exc_info=True)
        raise


if __name__ == '__main__':
    app_config = AppConfig()
    print(app_config)

    start_time = time.perf_counter()
    main(app_config)
    print()
    print(f"Done in {time.perf_counter() - start_time:.2f}s")
