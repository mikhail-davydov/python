class EasyDict(dict):
    def __getattr__(self, item):
        return self[item]


# alt

class EasyDict(dict):
    def __init__(self, d):
        super().__init__(d)
        self.__dict__ |= d

    def __setitem__(self, key, value):
        self.__dict__[key] = value


# alt

class EasyDict(dict):
    def __getattr__(self, key):
        return super().__getitem__(key)


# alt

class EasyDict(dict):
    __getattr__ = dict.__getitem__
