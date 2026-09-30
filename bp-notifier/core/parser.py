import logging
from datetime import datetime

from core.constants import DATE_FORMAT, NOTE_FIELDS_COUNT, SPLIT_BY
from core.models import InvoiceItem, InvoiceNoteInfo
from core.utils import to_number


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
            to_number(shelves),
        )
    except Exception as ex:
        logging.error(f'Ошибка при извлечении данных из invoice.note: {ex}', exc_info=True)
        return InvoiceNoteInfo(invoice.num, error=repr(ex))
