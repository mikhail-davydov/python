class Row:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            super().__setattr__(key, value)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')

        raise AttributeError('Установка нового атрибута невозможна')

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')

    def __repr__(self):
        attrs = ', '.join(f'{key}={value!r}' for key, value in self.__dict__.items())
        return f'{self.__class__.__name__}({attrs})'

    def __eq__(self, other):
        return self.__repr__() == other.__repr__() if isinstance(other, self.__class__) else NotImplemented

    def __hash__(self):
        return hash(self.__repr__())


# alt

class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @property
    def _fields(self):
        return tuple(self.__dict__.items())

    def __repr__(self):
        attrs = ', '.join(f'{name}={repr(value)}' for name, value in self._fields)
        return f'Row({attrs})'

    def __eq__(self, other):
        if isinstance(other, Row):
            return self._fields == other._fields
        return NotImplemented

    def __hash__(self):
        return hash(self._fields)

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError('Изменение значения атрибута невозможно')
        raise AttributeError('Установка нового атрибута невозможна')

    def __delattr__(self, name):
        raise AttributeError('Удаление атрибута невозможно')
