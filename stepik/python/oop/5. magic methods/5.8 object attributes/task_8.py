class ProtectedObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __getattribute__(self, item: str):
        if item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, item)


# alt

from functools import wraps


class ProtectedObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    @staticmethod
    def _check_protected(func):
        @wraps(func)
        def wrapper(self, item, *args, **kwargs):
            if item.startswith('_'):
                raise AttributeError('Доступ к защищенному атрибуту невозможен')
            return func(self, item, *args, **kwargs)

        return wrapper

    @_check_protected
    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    @_check_protected
    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

    @_check_protected
    def __delattr__(self, item):
        object.__delattr__(self, item)
