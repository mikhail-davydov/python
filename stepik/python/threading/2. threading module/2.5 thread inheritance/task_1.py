from threading import Thread

from typing import Callable


class MyThread(Thread):
    def __init__(self, msg_error: str = "error", task: Callable = None):
        super().__init__()
        self.msg_error = msg_error
        self.task = task

    def run(self) -> None:
        try:
            self.task()
        except Exception as err:
            print(self.msg_error)
