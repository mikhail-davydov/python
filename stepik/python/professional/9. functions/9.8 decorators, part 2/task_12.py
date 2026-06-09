class MaxRetriesException(Exception):
    pass


def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal times
            while times > 0:
                try:
                    return func(*args, **kwargs)
                except:
                    times -= 1
            raise MaxRetriesException()

        return wrapper

    return decorator


@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')


beegeek()

# alt # лучше использовать локальный счетчик
import functools


class MaxRetriesException(Exception):
    pass


def retry(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    pass
            raise MaxRetriesException

        return wrapper

    return decorator
