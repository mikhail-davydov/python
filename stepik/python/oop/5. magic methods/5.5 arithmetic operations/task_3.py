class SuperString:

    def __init__(self, string):
        self._string = string

    def __str__(self):
        return self._string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return __class__(self._string + other._string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return __class__(self._string * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            new_len = len(self._string) // other
            return __class__(self._string[:new_len])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            l = len(self._string)
            return __class__(self._string[:l - other]) if other < l else __class__('')
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            return __class__(self._string[other:]) if other < len(self._string) else __class__('')
        return NotImplemented


# alt
from functools import wraps


def decor(func):
    @wraps(func)
    def new_func(self, arg):
        if isinstance(arg, int):
            return func(self, arg)
        return NotImplemented

    return new_func


class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, new):
        if isinstance(new, str | self.__class__):
            return self.__class__(f"{self.string}{new}")
        return NotImplemented

    @decor
    def __mul__(self, n):
        return self.__class__(self.string * n)

    @decor
    def __truediv__(self, m):
        return self.__class__(self.string[:len(self.string) // m])

    @decor
    def __lshift__(self, n):
        return self.__class__('' if n > len(self.string) else self.string[:len(self.string) - n])

    @decor
    def __rshift__(self, n):
        return self.__class__(self.string[n:])

    __rmul__ = __mul__


s1 = SuperString('bee')
s2 = SuperString('geek')

print(s1 + s2)
print(s2 + s1)

print(10 * '-')

s = SuperString('beegeek')

print(s * 2)
print(3 * s)
print(s / 3)

print(10 * '-')

s = SuperString('beegeek')

print(s << 4)
print(s >> 3)

print(10 * '-')

s = SuperString('beegeek')
for i in range(9):
    print(f'{s} << {i} =', s << i)

print(10 * '-')

s = SuperString('beegeek')
for i in range(9):
    print(f'{s} >> {i} =', s >> i)
