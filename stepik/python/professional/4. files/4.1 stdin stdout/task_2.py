import sys
from datetime import date

dates = []
for line in sys.stdin:
    dates.append(date.fromisoformat(line.strip()))

min_dt = min(dates)
max_dt = max(dates)
print((max_dt - min_dt).days)