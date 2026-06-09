from typing import Iterable


class Peekable:
    def __init__(self, iterable: Iterable):
        self._iterable = iter(iterable)

    def peek(self, default: object = StopIteration):
        lst = list(self._iterable)
        if not lst:
            if default is not StopIteration:
                return default
            raise StopIteration
        value = lst[0]
        self._iterable = iter(lst)
        return value

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._iterable)


# alt

from copy import copy


class Peekable:
    def __init__(self, iterable):
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)

    def peek(self, default=StopIteration):
        iterator_peek = copy(self.iterator)

        if default != StopIteration:
            return next(iterator_peek, default)

        return next(iterator_peek)
