from operator import *  # импортируем все функции

print(add(10, 20))  # сумма
print(floordiv(20, 3))  # целочисленное деление
print(neg(9))  # смена знака
print(lt(2, 3))  # проверка на неравенство <
print(lt(10, 8))  # проверка на неравенство <
print(eq(5, 5))  # проверка на равенство ==
print(eq(5, 9))  # проверка на равенство ==

#

from functools import reduce
import operator

words = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']
numbers = [1, 2, -6, -4, 3, 9, 0, -6, -1]

opposite_numbers = list(map(operator.neg, numbers))  # смена знаков элементов списка
concat_words = reduce(operator.add, words)  # конкатенация элементов списка

print(opposite_numbers)
print(concat_words)

#

# Арифметические операции:

import operator as op

# Базовые арифметические
op.add(a, b)        # a + b
op.sub(a, b)        # a - b
op.mul(a, b)        # a * b
op.truediv(a, b)    # a / b  (обычное деление)
op.floordiv(a, b)   # a // b (целочисленное деление)
op.mod(a, b)        # a % b (остаток от деления)
op.pow(a, b)        # a ** b (возведение в степень)

# Унарные операции
op.neg(a)           # -a
op.pos(a)           # +a
op.abs(a)           # abs(a)
op.inv(a)           # ~a (инверсия)
op.invert(a)        # ~a (синоним)


# Битовые операции:

op.lshift(a, b)     # a << b
op.rshift(a, b)     # a >> b
op.and_(a, b)       # a & b
op.or_(a, b)        # a | b
op.xor(a, b)        # a ^ b


# Операции сравнения:

op.lt(a, b)         # a < b
op.le(a, b)         # a <= b
op.eq(a, b)         # a == b
op.ne(a, b)         # a != b
op.ge(a, b)         # a >= b
op.gt(a, b)         # a > b

# Проверка идентичности объектов
op.is_(a, b)        # a is b
op.is_not(a, b)     # a is not b


# Работа с последовательностями:

op.concat(a, b)     # a + b (для последовательностей)
op.contains(a, b)   # b in a
op.countOf(a, b)    # количество вхождений b в a
op.indexOf(a, b)    # индекс первого вхождения b в a

# Доступ к элементам
op.getitem(a, b)    # a[b]
op.setitem(a, b, c) # a[b] = c
op.delitem(a, b)    # del a[b]

# Срезы
op.getslice(a, b, c)    # a[b:c] (устаревшее)
op.setslice(a, b, c, d) # a[b:c] = d (устаревшее)
op.delslice(a, b, c)    # del a[b:c] (устаревшее)


# Функции для атрибутов:

op.attrgetter(attr)     # функция-геттер атрибута
op.attrgetter(*attrs)   # функция-геттер нескольких атрибутов

# Пример:
f = op.attrgetter('name', 'age')
name, age = f(person)


# Функции для элементов:

op.itemgetter(item)     # функция-геттер элемента
op.itemgetter(*items)   # функция-геттер нескольких элементов

# Пример:
f = op.itemgetter(2)    # получает 3-й элемент
f = op.itemgetter(1, 3) # получает 2-й и 4-й элементы


# Метод-вызыватели:

op.methodcaller(name)       # функция, вызывающая метод
op.methodcaller(name, *args, **kwargs)

# Пример:
f = op.methodcaller('upper')
result = f('hello')  # 'HELLO'

# Логические операции:

op.not_(a)          # not a
op.truth(a)         # True если a истинно, иначе False

# Эти функции возвращают первый аргумент, который определяет результат
op.and_(a, b)       # a and b
op.or_(a, b)        # a or b


# Получение полного списка:

import operator

# Получить все функции модуля
functions = [name for name in dir(operator)
             if not name.startswith('_') and callable(getattr(operator, name))]

print("Все функции operator:")
for func in sorted(functions):
    print(f"operator.{func}")

# Или сгруппировать по категориям
categories = {
    'Арифметика': ['add', 'sub', 'mul', 'truediv', 'floordiv', 'mod', 'pow', 'neg', 'pos', 'abs'],
    'Битовые': ['lshift', 'rshift', 'and_', 'or_', 'xor', 'inv', 'invert'],
    'Сравнение': ['lt', 'le', 'eq', 'ne', 'ge', 'gt', 'is_', 'is_not'],
    'Последовательности': ['concat', 'contains', 'countOf', 'indexOf', 'getitem', 'setitem', 'delitem'],
    'Утилиты': ['attrgetter', 'itemgetter', 'methodcaller', 'not_', 'truth']
}
