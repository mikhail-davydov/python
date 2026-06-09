from datetime import date

start = date.min.replace(day=13)
end = date.max.replace(day=13)

dict_13 = {}

while start < end:
    wd = start.weekday()
    dict_13[wd] = dict_13.get(wd, 0) + 1
    start = start.replace(month=start.month + 1) if start.month < 12 else start.replace(year=start.year + 1, month=1)

wd = end.weekday()
dict_13[wd] = dict_13.get(wd, 0) + 1

dict_13_sorted_by_key = dict(sorted(dict_13.items(), key=lambda item: item[0]))
print(*dict_13_sorted_by_key.values(), sep='\n')
