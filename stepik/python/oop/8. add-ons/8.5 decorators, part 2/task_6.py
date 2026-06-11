import functools


def auto_repr(args: list, kwargs: list):
    def decorator(cls):
        repr_origin = cls.__repr__

        @functools.wraps(repr_origin)
        def wrapper(self):
            args_attrs = [f'{getattr(self, arg)!r}' for arg in args]
            kwargs_attrs = [f'{arg}={getattr(self, arg)!r}' for arg in kwargs]
            attrs = ', '.join(args_attrs + kwargs_attrs)
            return f'{self.__class__.__name__}({attrs})'

        cls.__repr__ = wrapper
        return cls

    return decorator


# alt

def auto_repr(args, kwargs):
    def wrapper(cls):
        def __repr__(self):
            cls_args = [repr(self.__dict__[k]) for k in args]
            cls_kwargs = [f'{k}={self.__dict__[k]!r}' for k in kwargs]
            return f'{type(self).__name__}({", ".join(cls_args + cls_kwargs)})'

        cls.__repr__ = __repr__
        return cls

    return wrapper


# alt

class auto_repr:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, cls):
        def new_repr(inst):
            inst_args = [repr(inst.__dict__[arg]) for arg in self.args]
            inst_kwargs = [f"{arg}={inst.__dict__[arg]!r}" for arg in self.kwargs]
            inst_args.extend(inst_kwargs)
            return f"{cls.__name__}({', '.join(inst_args)})"

        cls.__repr__ = new_repr
        return cls
