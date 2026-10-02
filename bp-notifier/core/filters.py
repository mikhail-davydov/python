from abc import ABC
from datetime import date

from core.constants import WARN_NOTIFICATION_DAYS


class Filter(ABC):
    """
    Базовый класс для фильтрации данных
    """
    pass


class DaysToExpiredFilter(Filter):
    """
    Класс фильтрации по полю date_to
    Фильтрует записи в зависимости от значения параметра WARN_NOTIFICATION_DAYS (количество дней до истечения срока действия)
    """

    @staticmethod
    def apply(date_to: date) -> bool:
        now = date.today()
        days_diff = (date_to - now).days

        # Если WARN_NOTIFICATION_DAYS = 0 или None, пропускаем проверку (показываем всё)
        if WARN_NOTIFICATION_DAYS is not None and WARN_NOTIFICATION_DAYS > 0:
            return days_diff <= WARN_NOTIFICATION_DAYS

        return True


class RatePercentFilter(Filter):
    """
    Класс фильтрации InvoiceNoteInfo по значению "под реализацию" (проценты)
    """

    @staticmethod
    def apply() -> bool:
        pass
