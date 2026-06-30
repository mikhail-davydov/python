import threading

import time
from itertools import count

_count = count(1)


def my_initializer():
    print("Вызов initializer\n", end="")


def my_task():
    print("Вызов task\n", end="")


def my_test_permission():
    time.sleep(1)
    i = next(_count)
    print(f"Вызов permission {i} раз\n", end="")
    return i >= 4


# ----------Ваше решение
from typing import Callable


def run_task(event: threading.Event, initializer: Callable, task: Callable):
    initializer()
    event.wait()
    task()


def run_check_permission(event: threading.Event, permission: Callable):
    while not permission():
        pass
    event.set()


def delayed_launch(initializer: Callable, task: Callable, permission: Callable) -> None:
    event = threading.Event()
    threading.Thread(target=run_task, args=(event, initializer, task)).start()
    threading.Thread(target=run_check_permission, args=(event, permission)).start()


# -----------

start_time = time.perf_counter()

delayed_launch(my_initializer, my_task, my_test_permission)

if time.perf_counter() - start_time >= 0.01:
    print("Функция delayed_launch блокирует работу главного потока!")
