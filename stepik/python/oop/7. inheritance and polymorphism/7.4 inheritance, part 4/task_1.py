from collections import UserList


class DefaultList(UserList):

    def __init__(self, iterable=None, default=None):
        self.default = default
        super().__init__(iterable or list())

    def __getitem__(self, item):
        try:
            return self.data[item]
        except:
            return self.default
