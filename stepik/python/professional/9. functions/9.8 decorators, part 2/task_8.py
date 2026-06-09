def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return value if type(value) == datatype else TypeError

        return wrapper

    return decorator


@returns(list)
def beegeek():
    '''beegeek docs'''
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)

try:
    print(beegeek())
except TypeError as e:
    print(type(e))

# alt
import functools


def returns(datatype: type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if not isinstance(value, datatype):
                raise TypeError
            return value

        return wrapper

    return decorator
