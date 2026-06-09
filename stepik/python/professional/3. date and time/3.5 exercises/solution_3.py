from datetime import datetime, timedelta

pattern = '%d.%m.%Y %H:%M'
schedule = (
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=10), timedelta(hours=18)),
    (timedelta(hours=10), timedelta(hours=18))
)


def minutes_to_close(dt: datetime):
    current = timedelta(hours=dt.hour, minutes=dt.minute)
    current_schedule = schedule[dt.weekday()]
    return int(abs(current - current_schedule[1]).total_seconds() // 60) \
        if current_schedule[0] <= current < current_schedule[1] else 'Магазин не работает'


print(minutes_to_close(datetime.strptime(input(), pattern)))
