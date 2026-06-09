class HistoryDict:

    def __init__(self, data=()):
        self._data = dict(data)
        self._history_data = {}
        for key, item in self._data.items():
            self._history_data.setdefault(key, []).append(item)

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def history(self, item):
        return self._history_data.get(item, [])

    def all_history(self):
        return self._history_data

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        self._data[key] = value
        self._history_data.setdefault(key, []).append(value)

    def __delitem__(self, key):
        del self._data[key]
        del self._history_data[key]
