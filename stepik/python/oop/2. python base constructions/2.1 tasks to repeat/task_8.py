import calendar
from datetime import date


def get_fourth_thursday(year: int, month: int) -> date:
    cal = calendar.Calendar(firstweekday=calendar.MONDAY)
    weeks = cal.monthdatescalendar(year, month)
    thursdays = [week[3] for week in weeks if week[3].month == month]
    return thursdays[3]


year, month = int(input()), int(input())
fourth_thu = get_fourth_thursday(year, month)
print(fourth_thu.strftime('%d.%m.%Y'))

# alt
from datetime import date, timedelta

year, month = int(input()), int(input())
d = date(year, month, 1)

while d.isoweekday() != 4:
    d += timedelta(days=1)

d += timedelta(days=21)
print(d.strftime('%d.%m.%Y'))
