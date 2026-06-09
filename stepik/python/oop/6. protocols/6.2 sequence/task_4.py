from typing import Iterable


class OrderedSet:
    def __init__(self, iterable: Iterable = None):
        self._data = self._get_initial_data(iterable)

    def add(self, item):
        if item not in self._data:
            self._data.append(item)

    def discard(self, item):
        if item in self._data:
            self._data.remove(item)

    def _get_initial_data(self, iterable: Iterable) -> list:
        if iterable is None:
            return []
        lst = []
        for item in iterable:
            if item not in lst:
                lst.append(item)
        return lst

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __eq__(self, other):
        if isinstance(other, set):
            return set(self._data) == other
        if isinstance(other, self.__class__):
            return tuple(self._data) == tuple(other._data)
        return NotImplemented


# alt

class OrderedSet:
    def __init__(self, iterable=()):
        self._data = dict.fromkeys(iterable, None)

    def __len__(self):
        return len(self._data)

    def add(self, item):
        self._data.setdefault(item, None)

    def discard(self, item):
        self._data.pop(item, None)

    def __iter__(self):
        yield from self._data

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self._data) == len(other._data) and all(x == y for x, y in zip(self._data, other._data))
        if isinstance(other, set):
            return set(self._data) == other
        return NotImplemented
