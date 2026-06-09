class SparseArray:
    def __init__(self, default):
        self.array = {}
        self.default = default

    def __len__(self):
        return max(self.array)

    def __getitem__(self, key):
        return self.array.get(key, self.default)

    def __setitem__(self, key, value):
        self.array[key] = value


# alt

class SparseArray:
    def __init__(self, default):
        self._sequence = []
        self._default = default

    def __len__(self):
        return len(self._sequence)

    def __setitem__(self, key, value):
        if len(self) <= key:
            self._sequence += [self._default] * (key + 10)
        self._sequence[key] = value

    def __getitem__(self, key):
        if len(self) <= key:
            return self._default
        return self._sequence[key]
