class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__dict__['attrs_num'] = len(kwargs) + 1

    def __setattr__(self, key, value):
        self.__dict__['attrs_num'] = self.__dict__['attrs_num'] \
            if key in self.__dict__ \
            else self.__dict__['attrs_num'] + 1
        self.__dict__[key] = value

    def __delattr__(self, item):
        self.__dict__['attrs_num'] -= 1
        del self.__dict__[item]


# alt

class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, name):
        if name == 'attrs_num':
            return len(self.__dict__) + 1
