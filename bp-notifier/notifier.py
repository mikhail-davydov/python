from concurrent.futures import Future, ThreadPoolExecutor

import logging
import re
import sys
import time

from core.constants import (
    DOC_TYPE, MAX_WORKERS, SPLIT_BY, START_DATE, TIMEOUT
)
from core.filters import DaysToExpiredFilter
from core.models import AppConfig, InvoiceNoteInfo, ReportData
from core.parsers import InvoiceNoteInfoParser
from core.reports import SimpleOutputReport
from core.request import ArchiveRequest, DocInvoiceRequest

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(module)s %(funcName)s:%(lineno)d | %(message)s',
)


def main(config: AppConfig):
    try:
        invoices_total, invoice_ids = get_invoice_ids(config)
        logging.info(f'total: {invoices_total}, items={invoice_ids}')

        invoice_notes = get_invoice_notes(config, invoice_ids)
        valid_invoice_notes, invalid_invoice_notes, rate_invoice_notes = split_into_sublists(invoice_notes)
        shelves_total = sum(note.shelves for note in valid_invoice_notes)

        pending_invoice_notes = [
            invoice_note
            for invoice_note in valid_invoice_notes
            if DaysToExpiredFilter.apply(invoice_note.date_to)
        ]
        logging.info(f'{pending_invoice_notes=}')

        report_data = ReportData(
            invoices_total,
            shelves_total,
            pending_invoice_notes,
            valid_invoice_notes,
            invalid_invoice_notes,
            rate_invoice_notes,
        )

        SimpleOutputReport(report_data).make()
    except Exception as ex:
        logging.error(f'Exception: {ex}', exc_info=True)
        raise


def split_into_sublists(invoice_notes: list[InvoiceNoteInfo]):
    valid_invoice_notes: list[InvoiceNoteInfo] = []
    invalid_invoice_notes: list[InvoiceNoteInfo] = []
    rate_invoice_notes: dict = {}

    for invoice in invoice_notes:
        if error := invoice.error:
            split_error = tuple(map(str.strip, error.split(SPLIT_BY, 1)))
            reason, value = split_error[0], split_error[-1]
            if is_rate_based(reason, value):
                invoice.error = None
                invoice.rate = value.strip()
                rate_invoice_notes.setdefault(value, list())
                rate_invoice_notes[value].append(invoice.num)
            else:
                invalid_invoice_notes.append(invoice)
        else:
            valid_invoice_notes.append(invoice)

    return valid_invoice_notes, invalid_invoice_notes, rate_invoice_notes


def is_rate_based(reason, value):
    return reason and value and reason.strip() == 'Некорректный формат' and re.match(r'^\d+%$', value)


def get_invoice_notes(config: AppConfig, invoice_ids: list[str]) -> list[InvoiceNoteInfo]:
    max_workers = MAX_WORKERS or len(invoice_ids)
    invoice_req = DocInvoiceRequest(config.api_key, config.db, config.firm)

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

    invoice_notes = list(map(InvoiceNoteInfoParser.extract, invoices))
    return invoice_notes


def get_invoice_ids(config: AppConfig) -> tuple[int, list[str]]:
    archive_req = ArchiveRequest(config.api_key, config.db, config.firm)
    items = archive_req.get_full_doc_type_archive(DOC_TYPE, START_DATE)
    invoice_ids = [item.object for item in items]
    return len(invoice_ids), invoice_ids


if __name__ == '__main__':
    app_config = AppConfig()
    print(app_config)

    start_time = time.perf_counter()
    main(app_config)
    print()
    print(f"Done in {time.perf_counter() - start_time:.2f}s")
