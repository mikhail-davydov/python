from functools import singledispatchmethod


class Formatter:
    format_dict = {
        int: 'Целое число: {}',
        float: 'Вещественное число: {}',
        list: 'Элементы списка: {}',
        tuple: 'Элементы кортежа: {}',
        dict: 'Пары словаря: {}',
    }

    @singledispatchmethod
    @staticmethod
    def format(param):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register
    @staticmethod
    def _(param: int):
        print(Formatter.format_dict[type(param)].format(param))

    @format.register
    @staticmethod
    def _(param: float):
        print(Formatter.format_dict[type(param)].format(param))

    @format.register
    @staticmethod
    def _(param: list):
        list_format = ', '.join(map(str, param))
        print(Formatter.format_dict[type(param)].format(list_format))

    @format.register
    @staticmethod
    def _(param: tuple):
        tuple_format = ', '.join(map(str, param))
        print(Formatter.format_dict[type(param)].format(tuple_format))

    @format.register
    @staticmethod
    def _(param: dict):
        dict_format = ', '.join(map(str, param.items()))
        print(Formatter.format_dict[type(param)].format(dict_format))


# alt
class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def _(data):
        print(f'Целое число: {data}')

    @format.register(float)
    @staticmethod
    def _(data):
        print(f'Вещественное число: {data}')

    @format.register(tuple)
    @staticmethod
    def _(data):
        print(f'Элементы кортежа: {", ".join([str(obj) for obj in data])}')

    @format.register(list)
    @staticmethod
    def _(data):
        print(f'Элементы списка: {", ".join([str(obj) for obj in data])}')

    @format.register(dict)
    @staticmethod
    def _(data):
        print(f'Пары словаря: {", ".join([str(pair) for pair in data.items()])}')


Formatter.format(1337)
Formatter.format(20.77)

print(10 * '-')

Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))

print(10 * '-')

Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})

print(10 * '-')

try:
    Formatter.format('All them years, Dutch, for this snake?')
except TypeError as e:
    print(e)
