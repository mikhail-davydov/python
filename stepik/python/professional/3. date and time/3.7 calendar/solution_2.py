import calendar

year_str, month_abbr = input().split()
year = int(year_str)
month = list(calendar.month_abbr).index(month_abbr)

calendar.prmonth(year, month)