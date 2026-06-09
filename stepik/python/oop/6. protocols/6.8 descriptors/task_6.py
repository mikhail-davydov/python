class Versioned:
    def __set_name__(self, cls, attr):
        self._attr = attr
        self._attr_versions = f'{attr}_versions'

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, val):
        obj.__dict__[self._attr] = val
        obj.__dict__.setdefault(self._attr_versions, []).append(val)

    def get_version(self, obj, n):
        return obj.__dict__[self._attr_versions][n - 1]

    def set_version(self, obj, n):
        obj.__dict__[self._attr] = obj.__dict__[self._attr_versions][n - 1]
