import functools


class returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, self.datatype):
                raise TypeError
            return result

        return wrapper
