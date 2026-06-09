import calendar
from datetime import date


def get_days_in_month(year: int, month: str) -> list[date]:
    month_int = list(calendar.month_name).index(month)
    days = calendar.monthrange(year, month_int)[1]
    return [date(year, month_int, i) for i in range(1, days + 1)]


print(get_days_in_month(2021, 'December'))