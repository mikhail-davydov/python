from collections import UserString


class MutableString(UserString):
    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()
        # return self

    def sort(self, key=None, reverse=False):
        data_list = sorted(self.data, key=key, reverse=reverse)
        self.data = ''.join(data_list)

    def __setitem__(self, key, value):
        data_list = [c for c in self.data]
        data_list[key] = value
        self.data = ''.join(data_list)

    def __delitem__(self, key):
        data_list = [c for c in self.data]
        del data_list[key]
        self.data = ''.join(data_list)
