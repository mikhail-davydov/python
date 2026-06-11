def add_attr_to_class(*args, **kwargs):
    def decorator(cls):
        for key, value in kwargs.items():
            setattr(cls, key, value)
        return cls

    return decorator


# alt

class add_attr_to_class:
    def __init__(self, **kwargs):
        self.attrs = kwargs

    def __call__(self, cls):
        for attr_name, attr_value in self.attrs.items():
            setattr(cls, attr_name, attr_value)
        return cls
