from functools import reduce
from multiprocessing.managers import BaseManager
from operator import mul


class HandlerData:
    def __init__(self):
        self.data = []

    def get_sum(self):
        return sum(self.data)

    def get_mul(self):
        return reduce(mul, self.data)

    def send(self, args):
        self.data.extend(args)

    def clear(self):
        self.data = []

    def get_data(self):
        return self.data


class HandlerManager(BaseManager):
    pass
