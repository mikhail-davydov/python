import threading
from itertools import count
from time import sleep

count = count()


def trace_func(frame, event, arg):
    print(f"{next(count)} executing trace func with {threading.current_thread().name=}")
    print(f"{frame=}\n{event=}\n{arg=}")


def get_inform():
    print(f"{threading.current_thread().name=}")
    print(f"{threading.current_thread().ident=}")
    print(f"{threading.current_thread().native_id=}")
    print(f"{threading.get_ident()=}")
    print(f"{threading.get_native_id()=}")
    print("---------------")
    sleep(2)


threading.settrace(trace_func)

thr = [threading.Thread(target=get_inform) for _ in range(1)]
for t in thr:
    t.start()

# much better solution

import threading


def get_slow_inform():
    time.sleep(1.01)
    print(f"{threading.current_thread().name=}")


def profile_func():
    profiler = cProfile.Profile()
    profiler.enable()

    get_slow_inform()

    profiler.disable()
    profiler.print_stats(sort="time")


thr = threading.Thread(target=profile_func)
thr.start()
thr.join()

# and the best one

import threading
import cProfile
import time
from functools import wraps
from typing import Callable


def profile_func(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        profiler.print_stats(sort="time")
        return result

    return wrapper


@profile_func
def get_slow_inform():
    time.sleep(1.01)
    print(f"{threading.current_thread().name=}")


thr = threading.Thread(target=get_slow_inform)
thr.start()
thr.join()
