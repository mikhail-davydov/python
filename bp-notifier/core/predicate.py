from datetime import date

from core.constants import WARN_NOTIFICATION_DAYS


def should_include_invoice(date_to: date) -> bool:
    now = date.today()
    days_diff = (date_to - now).days

    # Если WARN_NOTIFICATION_DAYS = 0 или None, пропускаем проверку (показываем всё)
    if WARN_NOTIFICATION_DAYS is not None and WARN_NOTIFICATION_DAYS > 0:
        return days_diff <= WARN_NOTIFICATION_DAYS

    return True
