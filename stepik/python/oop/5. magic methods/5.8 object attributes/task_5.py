class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __setattr__(self, key, value):
        self.__dict__[key] = abs(value) if isinstance(value, (int, float)) else value


# alt

class NonNegativeObject:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __setattr__(self, name, value):
        if isinstance(value, (int, float)):
            value = abs(value)
        object.__setattr__(self, name, value)
