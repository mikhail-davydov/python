import calendar

year_str, month_name = input().split()
year = int(year_str)
month = list(calendar.month_name).index(month_name)

print(calendar.monthrange(year, month)[1])