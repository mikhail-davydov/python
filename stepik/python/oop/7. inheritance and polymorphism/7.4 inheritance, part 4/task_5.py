from collections import UserList


class NumberList(UserList):
    def __init__(self, initlist=None):
        if initlist is None:
            initlist = []
        all_nums = all(isinstance(item, (int | float)) for item in initlist)
        if not all_nums:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().__init__(initlist)

    def append(self, item):
        if not isinstance(item, (int | float)):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().append(item)

    def extend(self, other):
        all_nums = all(isinstance(item, (int | float)) for item in other)
        if not all_nums:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().extend(other)

    def insert(self, i, item):
        if not isinstance(item, (int | float)):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().insert(i, item)

    def __setitem__(self, key, value):
        if not isinstance(value, (int | float)):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().__setitem__(key, value)

    def __add__(self, other):
        all_nums = all(isinstance(item, (int | float)) for item in other)
        if not all_nums:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        return super().__iadd__(other)

    __iadd__ = __add__


# alt

class NumberList(UserList):
    def __init__(self, iterable=None):
        super().__init__(self._check_value(i) for i in iterable or [])

    @staticmethod
    def _check_value(value):
        if not isinstance(value, int | float):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        return value

    def __setitem__(self, index, value):
        super().__setitem__(index, self._check_value(value))

    def append(self, item):
        super().append(self._check_value(item))

    def extend(self, other):
        super().extend(self._check_value(i) for i in other)

    def insert(self, i: int, item):
        super().insert(i, self._check_value(item))

    def __add__(self, other):
        return super().__add__(self._check_value(i) for i in other)

    def __iadd__(self, other):
        return super().__iadd__(self._check_value(i) for i in other)
