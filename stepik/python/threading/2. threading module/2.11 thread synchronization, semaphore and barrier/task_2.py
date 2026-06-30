import threading
from typing import Callable


# допишите код

class HubHandler:
    def __init__(self, n: int, task: Callable, n_threads: int):
        self.semaphore = threading.Semaphore(n)
        self.task = task
        self.n_threads = n_threads

    def start_hub(self):
        threads = [threading.Thread(target=self._task_wrapper) for _ in range(self.n_threads)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def _task_wrapper(self):
        with self.semaphore:
            self.task()


# alt

class HubHendler:
    def __init__(self, n: int, task: Callable, n_threads: int):
        self.n = n
        self.task = task
        self.n_threads = n_threads
        self.semaphore = threading.Semaphore(self.n)

    def start_hub(self):
        for _ in range(self.n_threads):
            threading.Thread(target=self._executer).start()

    def _executer(self):
        with self.semaphore:
            self.task()
