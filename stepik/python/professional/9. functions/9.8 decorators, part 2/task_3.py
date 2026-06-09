import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        result = func(*args, **kwargs)
        print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(result)}')
        return result

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


say('Jane', 'Hello, World')
