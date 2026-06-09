import calendar

year, month, day = map(int, input().split('-'))
weekday = calendar.weekday(year, month, day)

print(list(calendar.day_name)[weekday])