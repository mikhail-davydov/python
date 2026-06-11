import functools


class singleton:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        klass = self.cls(*args, **kwargs)
        if self.instance is None:
            self.instance = klass
        self.instance.__dict__.update(klass.__dict__)
        return self.instance


# alt

def singleton(cls):
    cls_new = cls.__new__
    cls._instance = None

    @functools.wraps(cls_new)
    def new_for_singleton(*args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    cls.__new__ = new_for_singleton
    return cls
