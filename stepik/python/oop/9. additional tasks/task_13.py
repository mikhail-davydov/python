from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self, seq=None, **kwargs):
        super().__init__(seq, **kwargs)
        self._alias_count = 0

    def __delitem__(self, key):
        super().__delitem__(key)
        if key.endswith('_alias'):
            self._alias_count -= 1

    def __getitem__(self, key):
        return super().__getitem__(key)[0]

    def __len__(self):
        return len(self.data) - self._alias_count

    def __missing__(self, key):
        value = self.data.get(key + '_alias')
        if value is None:
            raise KeyError(key)
        return value

    def __setitem__(self, key, value):
        cur_value = self.data.get(key) or self.data.get(key + '_alias')
        if cur_value is None:
            cur_value = self.data.setdefault(key, [])
        cur_value[:] = [value]

    def alias(self, key, alias):
        self.data[alias + '_alias'] = self.data[key]
        self._alias_count += 1
