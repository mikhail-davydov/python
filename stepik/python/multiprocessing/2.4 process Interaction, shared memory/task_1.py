import multiprocessing


class MyProcess(multiprocessing.Process):
    def __init__(self, target=None, args=None):
        super().__init__()
        self.target = target
        self.args = args
        self.result = multiprocessing.Value("d", 0)

    def run(self):
        result = self.target(*self.args)
        self.result.value = result