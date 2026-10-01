from concurrent.futures import Future, ThreadPoolExecutor

import logging
import sys
import time

from core.constants import (
    DOC_TYPE, MAX_WORKERS, START_DATE, TIMEOUT
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

        all_invoice_notes = list(map(InvoiceNoteInfoParser.extract, invoices))

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
            if DaysToExpiredFilter.apply(invoice_note.date_to)
        ]
        logging.info(f'{pending_invoice_notes=}')

        report_data = ReportData(
            invoices_total,
            shelves_total,
            pending_invoice_notes,
            valid_invoice_notes,
            invalid_invoice_notes,
        )

        SimpleOutputReport(report_data).make()
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
