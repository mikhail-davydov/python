from typing import Iterable, Callable


class Grouper:
    def __init__(self, iterable: Iterable, key: Callable):
        self._iterable = iterable
        self._key = key
        self._data = {}
        for item in self._iterable:
            self.add(item)

            # alt
            # dict_key = self._key(item)
            # self._data.setdefault(dict_key, []).append(item)

    def add(self, item):
        key = self._key(item)
        self._data.setdefault(key, []).append(item)

    def group_for(self, item):
        return self._key(item)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data.items())

    def __getitem__(self, group):
        return self._data.get(group, [])

    def __contains__(self, group):
        return group in self._data
