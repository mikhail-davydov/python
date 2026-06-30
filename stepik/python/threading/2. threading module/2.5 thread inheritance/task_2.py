from collections.abc import Callable
from threading import Thread


class SimpleThread(Thread):
    def __init__(self, function: Callable, data):
        super().__init__()
        self.function = function
        self.data = data

    def run(self):
        print(self.function(self.data))
