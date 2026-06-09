class AdvancedList(list):
    def join(self, sep=' '):
        return sep.join(str(datum) for datum in self)

    def map(self, func):
        self[:] = list(map(func, self))

    def filter(self, func):
        self[:] = list(filter(func, self))


# alt

class AdvancedList(list):
    def __init__(self, iterable=(), default=None):
        super().__init__(item for item in iterable)
        self._default = default

    def extend_self(self, data):
        self.clear()
        self.extend(data)

    def join(self, sep=' '):
        return sep.join(str(item) for item in self)

    def map(self, func):
        new_data = list(func(item) for item in self)
        self.extend_self(new_data)

    def filter(self, predicate):
        new_data = list(filter(predicate, self))
        self.extend_self(new_data)
