from concurrent.futures import Future, ThreadPoolExecutor

import logging
import sys
import time
from datetime import date, datetime

from core.constants import (
    DATE_FORMAT, DOC_TYPE, MAX_WORKERS, NOTE_FIELDS_COUNT, SPLIT_BY, START_DATE, TIMEOUT, WARN_NOTIFICATION_DAYS
)
from core.models import AppConfig, InvoiceItem, InvoiceNoteInfo, Report
from core.request import ArchiveRequest, DocInvoiceRequest

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(module)s.%(funcName)s.%(lineno)d | %(message)s',
)


def should_include_invoice(date_to: date) -> bool:
    now = date.today()
    days_diff = (date_to - now).days

    # Если WARN_NOTIFICATION_DAYS = 0 или None, пропускаем проверку (показываем всё)
    if WARN_NOTIFICATION_DAYS is not None and WARN_NOTIFICATION_DAYS > 0:
        return days_diff <= WARN_NOTIFICATION_DAYS

    return True


def extract_invoice_fields(invoice: InvoiceItem) -> InvoiceNoteInfo:
    try:
        note = invoice.note
        if not note:
            logging.warning(f'#{invoice.num}: отсутствует note')
            return InvoiceNoteInfo(invoice.num, error='Отсутствует Примечание')

        parts = tuple(map(str.strip, invoice.note.split(SPLIT_BY)))
        if len(parts) < NOTE_FIELDS_COUNT:
            logging.warning(f'#{invoice.num}: некорректный формат, {invoice.note!r}')
            return InvoiceNoteInfo(invoice.num, error=f'Некорректный формат, {invoice.note!r}')

        name, phone, date_to, shelves = parts[:NOTE_FIELDS_COUNT]
        return InvoiceNoteInfo(
            invoice.num,
            name,
            phone,
            datetime.strptime(date_to, DATE_FORMAT).date(),
            int(shelves),
        )
    except Exception as ex:
        logging.error(f'Ошибка при извлечении данных из invoice.note: {ex}', exc_info=True)
        return InvoiceNoteInfo(invoice.num, error=repr(ex))


def print_invoice_report(report: Report):
    now = date.today()
    pending_total = len(report.pending_invoice_notes)
    valid_total = len(report.valid_invoice_notes)
    invalid_total = len(report.invalid_invoice_notes)

    print()
    print(f'Отчет за {now.strftime(DATE_FORMAT)}\n')
    print(f'Всех договоров: {report.invoices_total}')
    print(f'Активных договоров: {valid_total}')
    print(f'Занятых полок: {report.shelves_total}')
    print(f'Ошибок заполнения: {invalid_total}')
    print(f'Для обработки: {pending_total}\n')
    for note in sorted(report.pending_invoice_notes, key=lambda invoice_note: (invoice_note.date_to, invoice_note.num)):
        num, name, phone, date_to, shelves, _ = note
        days_diff = (date_to - now).days
        print(f'{'Договор #':<15s}: {num}')
        print(f'{'Имя':<15s}: {name}')
        print(f'{'Контакт':<15s}: {phone}')
        print(f'{'Действует до':<15s}: {date_to.strftime(DATE_FORMAT)}')
        print(f'{'Осталось дней':<15s}: {days_diff}{' (Просрочено)' if days_diff < 0 else ''}\n')

    if invalid_total:
        print('Ошибки заполнения:')
        for note in sorted(report.invalid_invoice_notes, key=lambda invoice_note: invoice_note.num):
            num, *_, error = note
            print(f'Договор # {num}: {error}')


def main(config: AppConfig):
    try:
        api_key = config.api_key
        db = config.db
        firm = config.firm

        archive_req = ArchiveRequest(api_key, db, firm)
        items = archive_req.get_full_doc_type_archive(DOC_TYPE, START_DATE)
        invoice_ids = [item.object for item in items]
        invoices_total = len(invoice_ids)
        logging.info(f'total: {invoices_total}, items={invoice_ids}')

        max_workers = MAX_WORKERS or len(invoice_ids)
        invoice_req = DocInvoiceRequest(api_key, db, firm)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            tasks: dict[Future, str] = {
                executor.submit(invoice_req.get_item, invoice): invoice
                for invoice in invoice_ids
            }

            invoices = []
            for task in tasks:
                try:
                    invoices.append(task.result(TIMEOUT))
                except Exception as ex:
                    logging.error(f'Get data failed for {tasks.get(task)}: {ex!r}', exc_info=True)

        all_invoice_notes = list(map(extract_invoice_fields, invoices))

        valid_invoice_notes: list[InvoiceNoteInfo] = []
        invalid_invoice_notes: list[InvoiceNoteInfo] = []
        for invoice in all_invoice_notes:
            if invoice.error:
                invalid_invoice_notes.append(invoice)
            else:
                valid_invoice_notes.append(invoice)

        shelves_total = sum(note.shelves for note in valid_invoice_notes)

        pending_invoice_notes = [
            invoice_note
            for invoice_note in valid_invoice_notes
            if should_include_invoice(invoice_note.date_to)
        ]
        logging.info(f'{pending_invoice_notes=}')

        report = Report(
            invoices_total,
            shelves_total,
            pending_invoice_notes,
            valid_invoice_notes,
            invalid_invoice_notes,
        )
        print_invoice_report(report)
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
