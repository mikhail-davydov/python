import functools


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(1, times):
                func(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')


say_beegeek()
