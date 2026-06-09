from typing import Iterable


class CyclicList:
    def __init__(self, iterable: Iterable = None):
        self._iterable = list(iterable) if iterable is not None else []
        self._index = -1

    def append(self, object):
        self._iterable.append(object)

    def pop(self, key=-1):
        value = self._iterable[key]
        del self._iterable[key]
        return value

    def __len__(self):
        return len(self._iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        return self._iterable[self._index % len(self)]

    def __getitem__(self, item):
        key = item % len(self)
        return self._iterable[key]


# alt
from itertools import cycle


class CyclicList:
    def __init__(self, iterable=()):
        self._data = list(iterable) or []

    def append(self, item):
        self._data.append(item)

    def pop(self, index=None):
        if index is None:
            return self._data.pop()
        return self._data.pop(index)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        yield from cycle(self._data)

    def __getitem__(self, index):
        return self._data[index % len(self._data)]
