import calendar
from datetime import date


def get_all_mondays(year: int) -> list[date]:
    return [date(year, month, week[0])
            for month in range(1, 13)
            for week in calendar.monthcalendar(year, month)
            if week[0] > 0]


print(get_all_mondays(2021))