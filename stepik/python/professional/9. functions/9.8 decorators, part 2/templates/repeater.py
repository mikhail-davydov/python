import functools


def repeater(repeat=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, repeat + 1):
                print(f'{i}-й запуск функции.')
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator


@repeater(repeat=5)
def beegeek():
    print('beegeek')


beegeek()


@repeater
def beegeek():
    print('beegeek')


beegeek()


@repeater()  # используется значение по умолчанию repeat=1
def beegeek():
    print('beegeek')


beegeek()
