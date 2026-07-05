import multiprocessing


class MinMaxAvr(multiprocessing.Process):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group, target, name, args, kwargs or {}, daemon=daemon)
        self.result = multiprocessing.Array("l", 3)

    def run(self):
        a, b, c = self._target(*self._args)
        self.result[0] = a
        self.result[1] = b
        self.result[2] = c
