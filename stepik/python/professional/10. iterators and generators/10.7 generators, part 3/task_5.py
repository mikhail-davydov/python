import datetime


def years_days(year):
    try:
        date = datetime.date(year, 1, 1)
        while date.year == year:
            yield date
            date = date + datetime.timedelta(days=1)
    except:
        pass


dates = years_days(2097)

print(*dates)

# alt
from datetime import date


def years_days(year):
    start = date(year, 1, 1)
    end = date(year + 1, 1, 1)
    return (date.fromordinal(i) for i in range(start.toordinal(), end.toordinal()))
