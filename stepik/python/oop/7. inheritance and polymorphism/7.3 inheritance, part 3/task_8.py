from typing import Iterable


class ModularTuple(tuple):
    def __new__(cls, iterable: Iterable = (), size: int = 100):
        return super().__new__(cls, map(lambda x: x % size, iterable))
