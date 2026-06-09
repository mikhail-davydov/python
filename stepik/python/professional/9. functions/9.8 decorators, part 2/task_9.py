def takes(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_cond = all(type(arg) in types for arg in args)
            kwargs_cond = all(type(kwarg) in types for kwarg in kwargs.values())
            if not args_cond or not kwargs_cond:
                raise TypeError
            return func(*args, **kwargs)

        return wrapper

    return decorator


@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times


try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))

# alt
import functools


def takes(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg in (*args, *kwargs.values()):
                if not isinstance(arg, types):
                    raise TypeError
            return func(*args, **kwargs)

        return wrapper

    return decorator
