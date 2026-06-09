import random


class RandomNumber:
    def __init__(self, start: int, end: int, cache: bool = False):
        self.start = start
        self.end = end
        self.cache = cache

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.cache and self._name in instance.__dict__:
            return instance.__dict__[self._name]
        instance.__dict__[self._name] = random.randint(self.start, self.end)
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        raise AttributeError('Изменение невозможно')


# alt

class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache
        self.value = random.randint(self.start, self.end)

    def __get__(self, obj, cls):
        if self.cache:
            return self.value
        return random.randint(self.start, self.end)

    def __set__(self, obj, value):
        raise AttributeError('Изменение невозможно')
