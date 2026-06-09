class FoodInfo:

    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        class_name = type(self).__name__
        attrs = self.proteins, self.fats, self.carbohydrates
        return f'{class_name}{attrs!r}'

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(
                self.proteins + other.proteins,
                self.fats + other.fats,
                self.carbohydrates + other.carbohydrates
            )
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(self.proteins * other, self.fats * other, self.carbohydrates * other)
        return NotImplemented

    def __truediv__(self, other):
        if other and isinstance(other, (int, float)):
            return FoodInfo(self.proteins / other, self.fats / other, self.carbohydrates / other)
        return NotImplemented

    def __floordiv__(self, other):
        if other and isinstance(other, (int, float)):
            return FoodInfo(self.proteins // other, self.fats // other, self.carbohydrates // other)
        return NotImplemented


# alt
class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def _as_tuple(self):
        return self.proteins, self.fats, self.carbohydrates

    def __repr__(self):
        return f'FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})'

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(*(s + v for s, v in zip(self._as_tuple(), other._as_tuple())))
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(*(i * other for i in self._as_tuple()))
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(*(i / other for i in self._as_tuple()))
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(*(i // other for i in self._as_tuple()))
        return NotImplemented


# alt
class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def _do_operation(self, op, n):
        ops = {
            '*': (lambda x: x * n),
            '/': (lambda x: x / n),
            '//': (lambda x: x // n),
        }

        return __class__(*map(ops[op], (self.proteins, self.fats, self.carbohydrates)))

    @staticmethod
    def _check_n(func):
        def wrapper(self, n):
            if isinstance(n, (int, float)):
                return func(self, n)
            return NotImplemented

        return wrapper

    def __repr__(self):
        return f'{__class__.__name__}({self.proteins}, {self.fats}, {self.carbohydrates})'

    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__(
                self.proteins + other.proteins,
                self.fats + other.fats,
                self.carbohydrates + other.carbohydrates
            )
        return NotImplemented

    @_check_n
    def __mul__(self, n):
        return self._do_operation('*', n)

    @_check_n
    def __truediv__(self, n):
        return self._do_operation('/', n)

    @_check_n
    def __floordiv__(self, n):
        return self._do_operation('//', n)


food1 = FoodInfo(10, 20, 30)
food2 = FoodInfo(10, 10, 20)

print(food1 + food2)
print(food1 * 2)
print(food1 / 2)
print(food1 // 2)

print(10 * '-')

food1 = FoodInfo(10, 20, 30)

try:
    food2 = (5, 10, 15) + food1
except TypeError:
    print('Некорректный тип данных')
