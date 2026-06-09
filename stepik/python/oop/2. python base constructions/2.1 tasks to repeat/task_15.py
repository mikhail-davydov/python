import functools


def recviz(func):
    indent = ' ' * 4
    indent_count = 0
    in_value = '->'
    out_value = '<-'

    def format_all_args(args, kwargs):
        args_formatted = ', '.join(
            f"'{arg}'" if isinstance(arg, str) else str(arg)
            for arg in args
        )

        kwargs_formatted = ', '.join(
            f"{k}='{v}'" if isinstance(v, str) else f'{k}={v}'
            for k, v in kwargs.items()
        )

        all_args_formatted = ''
        if args_formatted:
            all_args_formatted = f'{args_formatted}'
        if kwargs_formatted:
            all_args_formatted = f'{all_args_formatted}, {kwargs_formatted}'

        return all_args_formatted

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal indent_count

        all_args_formatted = format_all_args(args, kwargs)
        print(f'{indent_count * indent}{in_value} {func.__name__}({all_args_formatted})')
        indent_count += 1
        result = func(*args, **kwargs)
        result = f"'{result}'" if isinstance(result, str) else result
        indent_count -= 1
        print(f'{indent_count * indent}{out_value} {result}')

        return result

    return wrapper


# alt
def recviz(func):
    level = -1

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal level
        level += 1

        pos_args = list(map(repr, args))
        keyword_args = [f'{k}={v!r}' for k, v in kwargs.items()]

        print('    ' * level + '->', f'{func.__name__}({", ".join(pos_args + keyword_args)})')
        value = func(*args, **kwargs)
        print('    ' * level + '<-', repr(value))

        level -= 1
        return value

    return wrapper


@recviz
def add(a, b):
    return a + b


add(1, b=2)

print('-' * 10)


@recviz
def add(a, b, c, d, e):
    return (a + b + c) * (d + e)


add('a', b='b', c='c', d=3, e=True)

print('-' * 10)


@recviz
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(4)

print('-' * 10)


@recviz
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


fact(5)
