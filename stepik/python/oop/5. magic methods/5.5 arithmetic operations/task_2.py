class Vector:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __repr__(self):
        return '{}{}'.format(__class__.__name__, (self._x, self._y))

    def __add__(self, other):
        if isinstance(other, Vector):
            return __class__(self._x + other._x, self._y + other._y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return __class__(self._x - other._x, self._y - other._y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return __class__(self._x * other, self._y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return __class__(self._x / other, self._y / other)
        return NotImplemented


a = Vector(1, 2)
b = Vector(3, 4)

print(a + b)
print(a - b)
print(b + a)
print(b - a)

print(10 * '-')

a = Vector(3, 4)

print(a * 2)
print(2 * a)
print(a / 2)
