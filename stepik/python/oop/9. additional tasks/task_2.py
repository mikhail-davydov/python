import functools


def check_size(func):
    @functools.wraps(func)
    def wrapper(self, other):
        if len(self.coords) == len(other.coords):
            return func(self, other)
        raise ValueError('Векторы должны иметь равную длину')

    return wrapper


def check_type(func):
    @functools.wraps(func)
    def wrapper(self, other):
        if isinstance(other, self.__class__):
            return func(self, other)
        return NotImplemented

    return wrapper


class Vector:
    def __init__(self, *args):
        self.coords = args

    def norm(self):
        return sum(map(lambda x: x ** 2, self.coords)) ** 0.5

    def __str__(self):
        return str(self.coords)

    @check_type
    @check_size
    def __add__(self, other):
        return self.__class__(*[x + y for x, y in zip(self.coords, other.coords)])

    @check_type
    @check_size
    def __sub__(self, other):
        return self.__class__(*[x - y for x, y in zip(self.coords, other.coords)])

    @check_type
    @check_size
    def __mul__(self, other):
        return sum(x * y for x, y in zip(self.coords, other.coords))

    @check_type
    @check_size
    def __eq__(self, other):
        return self.coords == other.coords

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__


# alt

from functools import partialmethod
from operator import add, sub, mul, eq


class Vector:
    def __init__(self, *args):
        self.coords = args

    def __str__(self):
        return str(self.coords)

    def norm(self):
        return sum(digit ** 2 for digit in self.coords) ** 0.5

    def _generic(self, other, operation, func=None):
        if not isinstance(other, self.__class__):
            return NotImplemented
        if len(self.coords) != len(other.coords):
            raise ValueError("Векторы должны иметь равную длину")
        coords = map(operation, self.coords, other.coords)
        if func is not None:
            return func(coords)
        return self.__class__(*coords)

    __add__ = partialmethod(_generic, operation=add)
    __sub__ = partialmethod(_generic, operation=sub)
    __mul__ = partialmethod(_generic, operation=mul, func=sum)
    __eq__ = partialmethod(_generic, operation=eq, func=all)
