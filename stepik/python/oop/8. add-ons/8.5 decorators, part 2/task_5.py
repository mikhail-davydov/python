class snake_case:
    def __init__(self, attrs: bool = False):
        self.attrs = attrs

    def __call__(self, cls):
        orig_dict = dict(cls.__dict__)
        for key in orig_dict:
            value = getattr(cls, key)
            condition = (not str(key).startswith('__')) \
                if self.attrs \
                else (not str(key).startswith('__') and callable(value))
            if condition:
                new_key = '_'.join(map(str.lower, re.findall(rf'([a-zA-Z][a-z]*)', str(key))))
                if str(key).startswith('_'):
                    new_key = '_' + new_key
                setattr(cls, new_key, value)
                delattr(cls, key)
        return cls


# alt

from typing import Callable


def snake_case(attrs=False):
    regex_object = re.compile(r'_?\B([A-Z])')

    def wrapper(cls, *args, **kwargs):
        class_attributes = list(cls.__dict__.keys())
        for attribute in class_attributes:
            if any((
                    attribute.startswith('__') and attribute.endswith('__'),
                    not isinstance(cls.__dict__[attribute], Callable) and not attrs
            )
            ):
                continue
            setattr(cls, regex_object.sub(r'_\1', attribute).lower(), cls.__dict__[attribute])
            delattr(cls, attribute)
        return cls

    return wrapper


# alt

import re


def snake_case(attrs=False):
    def to_snake_case(string):
        return '_'.join(re.findall(r'[a-zA-Z][^A-Z]*', string)).lower()

    def decorator(cls):
        is_not_magic = lambda key, _: not key.startswith('__')
        is_method = lambda _, value: callable(value)
        tests = [is_not_magic]
        if not attrs:
            tests += [is_method]

        scheduled_for_update = []

        for item in cls.__dict__.items():
            if all(test(*item) for test in tests):
                scheduled_for_update.append(item)

        for key, value in scheduled_for_update:
            setattr(cls, to_snake_case(key), value)
            delattr(cls, key)

        return cls

    return decorator


# alt

from inflection import *


def snake_case(attrs=False):
    def wrapper(cls):
        attributes = [key for key in dir(cls) if not str(key).endswith('__')]  # Получаем список атрибутов и методов
        if not attrs:  # Если False - Вызываем и оставляем только методы
            attributes = [key for key in attributes if callable(getattr(cls, key))]
        for key in attributes:
            setattr(cls, underscore(key), getattr(cls, key))  # Устанавливаем новые ключи и значения
            delattr(cls, key)  # Удаляем старые
        return cls

    return wrapper
