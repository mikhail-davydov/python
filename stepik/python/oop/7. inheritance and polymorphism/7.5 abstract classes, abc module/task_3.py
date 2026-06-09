from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, value):
        raise NotImplemented

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._name in instance.__dict__:
            return instance.__dict__[self._name]
        raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self._name] = value


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        # super().__init__()
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int | float)):
            raise TypeError('Устанавливаемое значение должно быть числом')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
        return True


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        if self.predicate is not None and not self.predicate(value):
            raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')
        return True
