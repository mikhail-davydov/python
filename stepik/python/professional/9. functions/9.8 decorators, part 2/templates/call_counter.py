import random

import functools


def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.num += 1
        print(f'Вызов {func.__name__}: {wrapper.num}')
        val = func(*args, **kwargs)
        return val

    wrapper.num = 0
    return wrapper


@counter
def greet(name):
    return f'Hello {name}!'


@counter
def print_any_args(*args):
    print(*args)


print(greet('Timur'))
print(greet('Ruslan'))
print(greet('Arthur'))
print(greet('Gvido'))

print_any_args(range(1, 11))
print_any_args([str(random.randint(1, 10)) * 5 for _ in range(10)])
