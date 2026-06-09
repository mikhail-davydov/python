class RandomLooper:
    def __init__(self, *iterables):
        self._iterators = [iter(iterable) for iterable in iterables]

    def __iter__(self):
        return self

    def __next__(self):
        self.check_iterables_exist()
        idx = random.randint(0, len(self._iterators) - 1)
        try:
            return next(self._iterators[idx])
        except StopIteration:
            del self._iterators[idx]
            return self.__next__()

    def check_iterables_exist(self):
        if not self._iterators:
            raise StopIteration from None


# alt

import itertools as it
import random


class RandomLooper:
    def __init__(self, *args):
        self.iterables = list(it.chain(*args))
        self.length = len(self.iterables)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.length:
            raise StopIteration
        self.length -= 1
        ind = random.randint(0, self.length)
        return self.iterables.pop(ind)
