from collections.abc import Sequence

from typing import Iterable


class BitArray(Sequence):
    def __init__(self, iterable: Iterable = ()):
        self._data = list(iterable)

    def __str__(self):
        return str(self._data)

    def __getitem__(self, index):
        if isinstance(index, (int | slice)):
            return self._data[index]
        return NotImplemented

    def __len__(self):
        return len(self._data)

    def __invert__(self):
        return BitArray([1 - bit for bit in self._data])

    # Логические операции
    def __and__(self, other: "BitArray") -> "BitArray":
        if not isinstance(other, BitArray):
            return NotImplemented
        if len(self) != len(other):
            raise TypeError("BitArrays must be of the same length for bitwise operations")
        return BitArray([a & b for a, b in zip(self._data, other._data)])

    def __rand__(self, other: "BitArray") -> "BitArray":
        return self.__and__(other)

    def __or__(self, other: "BitArray") -> "BitArray":
        if not isinstance(other, BitArray):
            return NotImplemented
        if len(self) != len(other):
            raise TypeError("BitArrays must be of the same length for bitwise operations")
        return BitArray([a | b for a, b in zip(self._data, other._data)])

    def __ror__(self, other: "BitArray") -> "BitArray":
        return self.__or__(other)


# alt

class BitArray(list):
    def __invert__(self):
        return BitArray([abs(i - 1) for i in self])

    def __and__(self, other):
        if isinstance(other, __class__):
            return BitArray([i and j for i, j in zip(self, other)])
        else:
            return NotImplemented

    def __or__(self, other):
        if isinstance(other, __class__):
            return BitArray([i or j for i, j in zip(self, other)])
        else:
            return NotImplemented
