class PermaDict:
    def __init__(self, data: dict = None):
        data = data or {}
        self._data = {}
        self._data.update(data)

    # # alt
    # def __init__(self, data=()):
    #     self._data = dict(data) or {}

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        if key in self._data:
            raise KeyError('Изменение значения по ключу невозможно')
        self._data[key] = value

    def __delitem__(self, key):
        self._data.pop(key)
