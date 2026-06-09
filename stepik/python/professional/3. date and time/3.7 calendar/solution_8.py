import calendar
from datetime import date


def get_third_weekday_in_month(year: int, day: int = 0) -> list[str]:
    return list(
        map(lambda dt: dt.strftime('%d.%m.%Y'),
            [[date(year, month, week[day])
              for week in calendar.monthcalendar(year, month)
              if week[day] > 0][2]
             for month in range(1, 13)]
            )
    )


print(*get_third_weekday_in_month(int(input()), 3), sep='\n')
