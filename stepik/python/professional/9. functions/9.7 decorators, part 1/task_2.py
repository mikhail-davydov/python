def print_decorator(func):
    def wrapper(*args, **kwargs):
        args_upper = [str(arg).upper() for arg in args]
        kwargs_upper = {key: value.upper() for key, value in kwargs.items()}
        return func(*args_upper, **kwargs_upper)

    return wrapper

print = print_decorator(print)

print(111, 222, 333, sep='xxx')
