from typing import Callable


def sandwich(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        result = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return result

    return wrapper


@sandwich
def counter(*args, **kwargs):
    for i in args + tuple(kwargs.keys()) + tuple(kwargs.values()):
        print(i)


counter(10, 20, 30, sep='40', end='!!!', step='beegeek')


# alt
def sandwich(func):
    def wrapper(*args, **kwargs):
        try:
            print('---- Верхний ломтик хлеба ----')
            return func(*args, **kwargs)
        finally:
            print('---- Нижний ломтик хлеба ----')

    return wrapper
