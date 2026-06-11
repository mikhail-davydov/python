import functools


class type_check:
    def __init__(self, types: list):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            is_valid_types = all(type(arg) == arg_type for arg, arg_type in zip(args, self.types))
            if not is_valid_types:
                raise TypeError
            return func(*args, **kwargs)

        return wrapper


# alt

class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if all(map(isinstance, args, self.types)):
                return func(*args, **kwargs)
            raise TypeError

        return wrapper
