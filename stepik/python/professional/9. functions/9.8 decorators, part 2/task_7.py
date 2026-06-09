def strip_range(start: int, end: int, char: chr = '.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            chars_to_replace = min(end - start, len(value) - start)
            return value[:start] + char * chars_to_replace + value[end:]

        return wrapper

    return decorator


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'


print(beegeek())

# alt
import functools


def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            s = func(*args, **kwargs)
            return s[:start] + char * (min(end, len(s)) - start) + s[end:]

        return wrapper

    return decorator
