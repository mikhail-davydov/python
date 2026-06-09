import sys
from datetime import datetime

fmt = '%d.%m.%Y'

dates = [datetime.strptime(line.strip(), fmt) for line in sys.stdin]
sorted_dates = sorted(set(dates))
sorted_reversed_dates = sorted(set(dates), reverse=True)

print('ASC' if dates == sorted_dates else 'DESC' if dates == sorted_reversed_dates else 'MIX')
