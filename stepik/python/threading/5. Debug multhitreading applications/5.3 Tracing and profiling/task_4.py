import threading
from types import TracebackType
from typing import Callable


def custom_exception_handler(args):
    exc_type, exc_value, exc_tb, exc_thread = args
    exc_tb: TracebackType
    exc_thread: threading.Thread

    print(f'{exc_thread.name} (id={exc_thread.ident}) failed')


threading.excepthook = custom_exception_handler


class MyThread(threading.Thread):

    def __init__(self, target: Callable = None, result=None, args=None, kwargs=None):
        self._args = args or ()
        self._kwargs = kwargs or {}
        self._target = target
        self._result = result
        super().__init__(group=None, target=target, args=self._args, kwargs=self._kwargs)

    def run(self):
        current_ = threading.current_thread()
        if self._target is None:
            raise NoTargetException(current_.name)
        self._result = self._target(*self._args, **self._kwargs)


class NoTargetException(Exception):
    def __init__(self, thread_name):
        super().__init__(f'{thread_name} has no target')
