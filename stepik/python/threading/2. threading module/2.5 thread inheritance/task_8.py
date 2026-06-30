# Ваше решение
import functools

import threading

import time
from collections.abc import Callable
from typing import Any


class ConcurrentExecutor:
    def __init__(self):
        self._threads: list[threading.Thread] = []
        self._results: dict[str, Any] = {}

    def concurrent_run(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=self._thread_wrapper, args=(func, args, kwargs), daemon=True)
            thread.start()
            self._threads.append(thread)

        return wrapper

    def get_results(self, timeout=None) -> dict[str, Any]:
        if timeout:
            time.sleep(timeout)
        else:
            for thread in self._threads:
                thread.join()
        return self._results

    def _thread_wrapper(self, func: Callable, args, kwargs):
        try:
            self._results |= {func.__name__: func(*args, **kwargs)}
        except Exception as exc:
            self._results |= {func.__name__: repr(exc)}


# Работа тестирующей системы
executor = ConcurrentExecutor()


@executor.concurrent_run
def task1(n: int):
    time.sleep(n)
    return f"result={n}"


@executor.concurrent_run
def task2(n: int, name: str):
    time.sleep(n)
    print("Ошибка! Этот текст не должен быть напечатан, не ждите завершение работы дольше таймаута!")
    return f"result={n}"


@executor.concurrent_run
def task3(name: str, n: int):
    time.sleep(n)
    raise ValueError("oops!")


start_time = time.perf_counter()
task1(2)
task2(4, "Romulus")
task3("Remus", 1)
msg = "Декорируемые функции не должны блокировать выполнение главного потока!"
assert time.perf_counter() - start_time < 0.1, msg

start_time = time.perf_counter()
for func, result in executor.get_results(2.1).items():
    print(f"{func} => {result}")
msg = "get_results должен ограничивать ожидание завершения работы декорируемых функций!"
assert time.perf_counter() - start_time < 2.2, msg


# alt

class ConcurrentExecutor:
    def __init__(self):
        self.threads = []
        self.results = {}

    def concurrent_run(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def thread_func():
                try:
                    result = func(*args, **kwargs)
                except Exception as exc:
                    result = repr(exc)
                finally:
                    self.results[func.__name__] = result

            thread = threading.Thread(target=thread_func, daemon=True)
            self.threads.append(thread)
            thread.start()

        return wrapper

    def get_results(self, timeout=None) -> dict[str, Any]:
        if not self.threads:
            return {}
        else:
            deadline = time.perf_counter() + timeout if timeout is not None else None
            for thread in self.threads:
                thread.join(deadline - time.perf_counter() if deadline else None)
        return self.results
