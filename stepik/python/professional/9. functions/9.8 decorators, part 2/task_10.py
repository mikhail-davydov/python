def add_attrs(**func_kwargs):
    def decorator(func):
        for key, value in func_kwargs.items():
            func.__dict__[key] = value

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)

# alt #1
'''
Почему wrapper.__dict__ |= attrs, а не func.__dict__ |= attrs?


func — это оригинальная функция, и её __dict__ изменять нельзя и некорректно в контексте декоратора:

Изменение func.__dict__ повлияет на саму функцию глобально.
Если функция используется в других местах, это может вызвать побочные эффекты.
Декоратор должен быть прозрачным и не модифицировать оригинал.

wrapper — это обёртка, которую мы возвращаем как "новую" функцию.

Мы хотим, чтобы у wrapper были те же атрибуты, что и у func, но без изменения func.
Поэтому правильно копировать атрибуты из func в wrapper.
'''

import functools


def add_attrs(**attrs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.__dict__ |= attrs
        return wrapper

    return decorator


# alt #2
def add_attrs(**attrs):
    def decorator(func):
        func.__dict__.update(attrs)
        return func

    return decorator
