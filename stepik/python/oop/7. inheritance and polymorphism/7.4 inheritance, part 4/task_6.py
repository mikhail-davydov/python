class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k
        return None

    def keys_of(self, value):
        return (k for k, v in self.items() if v == value)


# alt

class ValueDict(dict):
    def key_of(self, value):
        return next(self.keys_of(value), None)

    def keys_of(self, value):
        return (i for i, j in self.items() if j == value)
