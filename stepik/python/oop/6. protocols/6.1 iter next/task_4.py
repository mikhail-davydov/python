from typing import Iterable


class SkipIterator:
    def __init__(self, iterable: Iterable, n: int):
        self.iterable = iter(iterable)
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.iterable)
        try:
            for _ in range(self.n):
                next(self.iterable)
        except:
            pass
        return value


# alt

class SkipIterator:
    def __init__(self, iterable, n):
        self.obj = iter(list(iterable)[::n + 1])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.obj)
