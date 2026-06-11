import functools


def track_instances(cls):
    old_init = cls.__init__
    cls.instances = []

    @functools.wraps(old_init)
    def decorator(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.instances.append(self)

    cls.__init__ = decorator
    return cls


# alt

def track_instances(cls):
    cls.instances = []

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        cls.instances.append(instance)
        return instance

    return wrapper


# alt

class track_instances:
    instances = []

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        instanse = self.cls(*args, **kwargs)
        self.instances.append(instanse)
        return instanse
