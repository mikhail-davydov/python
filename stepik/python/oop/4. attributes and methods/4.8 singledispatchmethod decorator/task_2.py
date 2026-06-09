from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(param):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _num_neg(param):
        return -param

    @neg.register(bool)
    @staticmethod
    def _bool_neg(param):
        return not param


# alt
class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register
    @staticmethod
    def _(data: int | float):
        return -data

    @neg.register
    @staticmethod
    def _(data: bool):
        return not data


print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))

print(10 * '-')

try:
    Negator.neg('number')
except TypeError as e:
    print(e)
