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
        rate_total = sum(map(len, self.report_data.rate_invoice_notes.values()))

        print()
        print(f'Отчет за {now.strftime(DATE_FORMAT)}\n')
        print(f'Всего договоров: {self.report_data.invoices_total}')
        print(f'Активных: {valid_total}')
        print(f'Занятых полок: {self.report_data.shelves_total}')
        print(f'Под реализацию: {rate_total}')
        print(f'Ошибок заполнения: {invalid_total}')
        print(f'Для обработки: {pending_total}\n')
        for note in sorted(self.report_data.pending_invoice_notes,
                           key=lambda invoice_note: (invoice_note.date_to, invoice_note.num),
                           ):
            days_diff = (note.date_to - now).days
            print(f'{'Договор #':<15s}: {note.num}')
            print(f'{'Имя':<15s}: {note.name}')
            print(f'{'Контакт':<15s}: {note.phone}')
            print(f'{'Действует до':<15s}: {note.date_to.strftime(DATE_FORMAT)}')
            print(f'{'Осталось дней':<15s}: {days_diff}{' (Просрочено)' if days_diff < 0 else ''}\n')

        if rate_total:
            print('Под реализацию:')
            for rate, invoices in sorted(self.report_data.rate_invoice_notes.items()):
                print(f'Ставка {rate}, договора: {', '.join(map(str, sorted(invoices)))}')
            print()

        if invalid_total:
            print('Ошибки заполнения:')
            for note in sorted(self.report_data.invalid_invoice_notes, key=lambda invoice_note: invoice_note.num):
                print(f'Договор # {note.num}: {note.error}')
