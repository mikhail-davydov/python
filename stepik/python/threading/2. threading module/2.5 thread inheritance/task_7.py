# Ваше решение
from itertools import count

from collections.abc import Callable
from functools import wraps


class ConcurrentExecutor:
    def __init__(self):
        self.counter = 0

    def concurrent_run(self, func: Callable) -> Callable:
        self.counter += 1
        thread_name = f'ConcurrentExecutor#{self.counter} [{func.__name__}]'

        def wrapper(*args, **kwargs):
            threading.Thread(target=func, name=thread_name, args=args, kwargs=kwargs).start()

        return wrapper


# alt

class ConcurrentExecutor:
    def __init__(self):
        self.count = count(1)

    def concurrent_run(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            threading.Thread(
                target=func, args=args, kwargs=kwargs, name=f"ConcurrentExecutor#{next(self.count)} [{func.__name__}]",
            ).start()

        return wrapper


# Работа тестирующей системы
import time
import threading

executor = ConcurrentExecutor()


@executor.concurrent_run
def task1(n: int):
    time.sleep(n)
    print(f"{threading.current_thread().name} done!")


@executor.concurrent_run
def task2(n: int, name: str):
    time.sleep(n)
    print(f"{threading.current_thread().name} done!")


@executor.concurrent_run
def task3(name: str, n: int):
    time.sleep(n)
    print(f"{threading.current_thread().name} done!")


start_time = time.perf_counter()
task1(2)
task2(3, "Romulus")
task3("Remus", 1)
msg = "Декорируемые функции не должны блокировать выполнение главного потока!"
assert time.perf_counter() - start_time < 0.1, msg
