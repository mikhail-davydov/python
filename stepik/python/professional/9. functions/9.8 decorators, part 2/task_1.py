import functools


def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return value ** 2

    return wrapper


@square
def add(a, b):
    '''прекрасная функция'''
    return a + b

print(add(1, 1))
print(add.__name__)
print(add.__doc__)
