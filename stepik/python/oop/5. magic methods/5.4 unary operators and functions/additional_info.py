# Для округления числа decimal.Decimal
import decimal

decimal.getcontext().prec = 3
s = decimal.Decimal('1.23456789')
print(s)
print(+s)  # + вызывает округление
print(s == +s)

# (Python 3.3 и новее) Для удаления ключей с неположительными значениями в collections.Counter
from collections import Counter

c = Counter(a=2, b=-4, c=0)

print(c)
print(+c)

# Создаёт копию объекта (пример с numpy.array)
from numpy import array

s = array([1, 2, 3])

plus_a = +s
a = s

s[0] = 0

print(f"s:      {s}")
print(f"a:      {a}")
print(f"plus_a: {plus_a}")


# Из-за того, что унарный плюс возвращает копию объекта, вы можете копировать свои объекты (если у вас не синглтон)
class Cat:
    def __init__(self, name) -> None:
        self.name = name

    def __pos__(self):
        return Cat(self.name)


bar = Cat("Barsik")
fake_bar = +bar
copy_bar = bar

print(bar is fake_bar)  # False
print(bar is copy_bar)  # True
