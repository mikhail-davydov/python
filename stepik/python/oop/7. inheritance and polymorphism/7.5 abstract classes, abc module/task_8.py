from collections import UserList

from collections.abc import Sequence
from typing import Iterable


class SortedList(UserList):
    def __init__(self, iterable: Iterable = ()):
        super().__init__()
        self.data = sorted(iterable)

    def add(self, item):
        self.data = sorted(self.data + [item])

    def discard(self, item):
        for _ in range(self.data.count(item)):
            self.data.remove(item)

    def update(self, iterable: Iterable = ()):
        self.data = sorted(self.data + list(iterable))

    def append(self, item):
        raise NotImplementedError

    def extend(self, other):
        raise NotImplementedError

    def insert(self, i, item):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __getitem__(self, index):
        if isinstance(index, (int, slice)):
            return self.data[index]
        return NotImplemented

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.data})'

    def __reversed__(self):
        raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, int):
            return SortedList(self.data * other)
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            self.data = sorted(self.data * other)
            return self
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, SortedList):
            return SortedList(self.data + other.data)
        elif isinstance(other, Sequence):
            return SortedList(self.data + list(other))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, SortedList):
            self.data = sorted(self.data + other.data)
            return self
        elif isinstance(other, Sequence):
            self.data = sorted(self.data + list(other))
            return self
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Sequence):
            return self.data < list(other)
        return NotImplemented


# alt

from bisect import bisect_left, bisect_right, insort
from collections.abc import MutableSequence


class SortedList(MutableSequence):
    def __init__(self, iterable=()):
        self._data = sorted(iterable)

    def add(self, obj):
        insort(self._data, obj)

    def discard(self, obj):
        left = bisect_left(self._data, obj)
        right = bisect_right(self._data, obj)
        self._data[left:right] = []

    def update(self, iterable):
        for it in iterable:
            self.add(it)

    def __getitem__(self, index):
        return self._data[index]

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data

    def __iter__(self):
        yield from self._data

    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._data + other._data)
        return NotImplemented

    def __iadd__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        self.update(other._data)
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            return type(self)(self._data * other)
        return NotImplemented

    def __imul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self._data.clear() if other <= 0 else self.update(self._data * (other - 1))
        return self

    def __repr__(self):
        return f'SortedList({self._data})'

    def append(self, value):
        raise NotImplementedError

    def insert(self, index, value):
        raise NotImplementedError

    def extend(self, values):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError

    def __setitem__(self, key, value):
        raise NotImplementedError
