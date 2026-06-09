class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._attr = name
        self._default = default

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = instance.__dict__.get(self._attr, self._default)
        if value is None:
            raise AttributeError('Атрибут не найден')
        return value

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Некорректное значение')
        instance.__dict__[self._attr] = value
