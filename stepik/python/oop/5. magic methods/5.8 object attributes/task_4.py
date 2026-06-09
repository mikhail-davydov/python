class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__.update(kwargs)

    def __getattribute__(self, item):
        return super().__getattribute__(item)

    def __getattr__(self, item):
        return self.default


# alt
class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__.update(kwargs)

    def __getattr__(self, name):
        return self.default
