from functools import total_ordering


@total_ordering
class Month:

    def __init__(self, year: int, month: int):
        self._year_month = year, month

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._year_month == other._year_month
        if isinstance(other, tuple):
            return self._year_month == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self._year_month < other._year_month
        if isinstance(other, tuple):
            return self._year_month < other
        return NotImplemented

    def __str__(self):
        return '-'.join(map(str, self._year_month))

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}{self._year_month!r}'


print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))

print(10 * '-')

months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]
print(sorted(months))

print(10 * '-')

months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]
print(min(months))
print(max(months))
