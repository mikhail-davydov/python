import functools


class ignore_exception:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if e.__class__ in self.exceptions:
                    print(f'Исключение {e.__class__.__name__} обработано')
                    return None
                raise

        return wrapper


# alt

class ignore_exception:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                return value
            except self.exceptions as e:
                print(f'Исключение {e.__class__.__name__} обработано')

        return wrapper
