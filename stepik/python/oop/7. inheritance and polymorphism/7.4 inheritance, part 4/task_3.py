from collections import UserDict


class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data[key] = value
        self.data[value] = key


# alt

class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data.__setitem__(key, value)
        self.data.__setitem__(value, key)
