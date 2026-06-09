def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result
        raise TypeError

    return wrapper


@returns_string
def add(a, b):
    return a + b


try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))

# alt
import functools


def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return '' + func(*args, **kwargs)

    return wrapper
