import datetime

from datetime import date


def dates(start, count=None):
    try:
        idx = 0
        while idx != count:
            yield start + datetime.timedelta(days=idx)
            idx += 1
    except:
        return


generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print('Error')

# alt
from datetime import date, timedelta


def dates(start, count=None):
    count = count or (date.max - start).days + 1
    for i in range(count):
        yield start + timedelta(days=i)
        