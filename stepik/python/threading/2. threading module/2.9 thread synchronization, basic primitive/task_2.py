import functools

import threading

lock = threading.Lock()


def with_lock(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        with lock:
            return func(*args, **kwargs)

    return inner
