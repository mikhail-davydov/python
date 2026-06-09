class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name}: {self.dict_repr(self.__dict__)}'

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.dict_repr(self.__dict__)})'

    @staticmethod
    def dict_repr(dct: dict):
        return ', '.join((f'{k}={v!r}' for k, v in dct.items()))


# alt
class AnyClass:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return f'AnyClass: {", ".join(self._attrs())}'

    def __repr__(self):
        return f'AnyClass({", ".join(self._attrs())})'

    def _attrs(self):
        return [f'{k}={repr(v)}' for (k, v) in self.__dict__.items()]


any = AnyClass()

print(str(any))
print(repr(any))

print(10 * '-')

cowboy = AnyClass(name='John', surname='Marston')

print(str(cowboy))
print(repr(cowboy))

print(10 * '-')

obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))
