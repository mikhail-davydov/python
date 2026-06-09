import functools


def prefix(string: str, to_the_end: bool = False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result) + string if to_the_end else string + str(result)

        return wrapper

    return decorator


@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'


print(get_bonus())
