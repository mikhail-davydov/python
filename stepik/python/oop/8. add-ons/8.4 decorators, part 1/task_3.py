import functools


class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        args_cond = all(isinstance(arg, (int | float)) for arg in args)
        kwargs_cond = all(isinstance(arg, (int, float)) for arg in kwargs.values())
        if not (args_cond and kwargs_cond):
            raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)


# alt

class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        for i in [*args, *kwargs.values()]:
            if not isinstance(i, (float, int)):
                raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)
