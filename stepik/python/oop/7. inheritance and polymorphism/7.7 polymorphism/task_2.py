from abc import ABC, abstractmethod
from typing import Iterable


class Stat(ABC):
    def __init__(self, iterable: Iterable = ()):
        self.iterable = list(iterable)

    def add(self, item):
        self.iterable.append(item)

    @abstractmethod
    def result(self):
        return NotImplemented

    def clear(self):
        self.iterable.clear()


class MinStat(Stat):
    def result(self):
        if not self.iterable:
            return None
        return min(self.iterable)


class MaxStat(Stat):
    def result(self):
        if not self.iterable:
            return None
        return max(self.iterable)


class AverageStat(Stat):
    def result(self):
        if not self.iterable:
            return None
        return sum(self.iterable) / len(self.iterable)


# alt

import statistics
from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def add(self, n):
        self.data.append(n)

    def clear(self):
        self.data.clear()

    @abstractmethod
    def result(self):
        pass


class MinStat(Stat):
    def result(self):
        return min(self.data, default=None)


class MaxStat(Stat):
    def result(self):
        return max(self.data, default=None)


class AverageStat(Stat):
    def result(self):
        return statistics.fmean(self.data) if self.data else None
