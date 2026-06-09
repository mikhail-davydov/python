from collections.abc import Collection
from copy import deepcopy, copy


class Atomic:
    def __init__(self, data: Collection, deep: bool = False):
        self.data = data
        self.data_copy = deepcopy(self.data) if deep else copy(self.data)

    def __enter__(self):
        return self.data_copy

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            if isinstance(self.data, list):
                self.data[:] = self.data_copy
            if isinstance(self.data, (set | dict)):
                self.data.clear()
                self.data.update(self.data_copy)
        return True


# alt

class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self.deep = deep
        self.copy = deepcopy(self.data) if deep else copy(self.data)

    def __enter__(self):
        return self.copy

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is None:
            self.data.clear()
            if isinstance(self.data, list):
                self.data.extend(self.copy)
            else:
                self.data.update(self.copy)
        return True


# alt

class Atomic:
    def __init__(self, data, deep=False):
        self.original = data
        self.copy = deepcopy if deep else copy

        if isinstance(data, list):
            self.original_update = self.original.extend
        elif isinstance(data, (set, dict)):
            self.original_update = self.original.update

    def __enter__(self):
        self.data = self.copy(self.original)
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.original.clear()
            self.original_update(self.data)
        return True
