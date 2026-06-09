def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), 'Функция выполнилась без ошибок'
        except Exception:
            return None, 'При вызове функции произошла ошибка'

    return wrapper


@exception_decorator
def f(x):
    return x**2 + 2*x + 1

print(f(7))