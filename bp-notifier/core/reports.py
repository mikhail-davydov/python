from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date

from core.constants import DATE_FORMAT
from core.models import ReportData


@dataclass
class Report(ABC):
    """
    Базовый класс для отчетов
    """

    report_data: ReportData

    @abstractmethod
    def make(self):
        raise NotImplemented


@dataclass
class SimpleOutputReport(Report):
    """
    Простой отчет с выводом в sys.stdout
    """

    def make(self):
        now = date.today()
        pending_total = len(self.report_data.pending_invoice_notes)
        valid_total = len(self.report_data.valid_invoice_notes)
        invalid_total = len(self.report_data.invalid_invoice_notes)

        print()
        print(f'Отчет за {now.strftime(DATE_FORMAT)}\n')
        print(f'Всего договоров: {self.report_data.invoices_total}')
        print(f'Активных: {valid_total}')
        print(f'Занятых полок: {self.report_data.shelves_total}')
        print(f'Ошибок заполнения: {invalid_total}')
        print(f'Для обработки: {pending_total}\n')
        for note in sorted(self.report_data.pending_invoice_notes,
                           key=lambda invoice_note: (invoice_note.date_to, invoice_note.num),
                           ):
            num, name, phone, date_to, shelves, _ = note
            days_diff = (date_to - now).days
            print(f'{'Договор #':<15s}: {num}')
            print(f'{'Имя':<15s}: {name}')
            print(f'{'Контакт':<15s}: {phone}')
            print(f'{'Действует до':<15s}: {date_to.strftime(DATE_FORMAT)}')
            print(f'{'Осталось дней':<15s}: {days_diff}{' (Просрочено)' if days_diff < 0 else ''}\n')

        if invalid_total:
            print('Ошибки заполнения:')
            for note in sorted(self.report_data.invalid_invoice_notes, key=lambda invoice_note: invoice_note.num):
                num, *_, error = note
                print(f'Договор # {num}: {error}')
