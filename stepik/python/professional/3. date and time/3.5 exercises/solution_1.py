from datetime import date, time, datetime, timedelta


def str_to_timedelta(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return timedelta(hours=hours, minutes=minutes)


data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

total = timedelta()

for start, end in data:
    start_dt = str_to_timedelta(start)
    end_dt = str_to_timedelta(end)
    total += (end_dt - start_dt)

print(total.seconds // 60)
