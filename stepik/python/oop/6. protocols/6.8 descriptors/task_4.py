class TypeChecked:
    def __init__(self, *classes):
        self._classes = classes

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._name not in instance.__dict__:
            raise AttributeError('Атрибут не найден')
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if type(value) not in self._classes:
            raise TypeError('Некорректное значение')
        instance.__dict__[self._name] = value

    # alt
    # def __set__(self, obj, value):
    #     if not isinstance(value, self._types):
    #         raise TypeError('Некорректное значение')
    #     obj.__dict__[self._attr] = value