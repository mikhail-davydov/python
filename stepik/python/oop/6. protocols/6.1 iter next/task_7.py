from copy import copy

from typing import Iterable


class LoopTracker:
    def __init__(self, iterable: Iterable):
        self._iterable = iter(iterable)
        self._accesses = 0
        self._empty_accesses = 0
        self._first = next(iter(iterable)) if iterable else None
        self._last = None

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if self._first is None:
            raise AttributeError('Исходный итерируемый объект пуст')
        return self._first

    @property
    def last(self):
        if self._last is None:
            raise AttributeError('Последнего элемента нет')
        return self._last

    def is_empty(self):
        try:
            iter_copy = copy(self._iterable)
            next(iter_copy)
            return False
        except StopIteration:
            return True

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = next(self._iterable)
            self._accesses += 1
            self._last = value
            return value
        except StopIteration:
            self._empty_accesses += 1
            raise
