import threading
from itertools import count
from typing import Callable


class TestWorker(threading.Thread):
    def __init__(self, task: Callable, permission: Callable):
        super().__init__()
        self.permission = permission
        self.task = task
        self.condition = threading.Condition()

    def make_work(self):  # основной метод выполняет задачу если получено условие
        with self.condition:
            tmp = self.condition.wait_for(predicate=self.permission, timeout=1)
            if tmp:
                self.task()  # выполняем задачу если разрешено
            else:
                # не выполняем задачу, просто логируем, что не дождались условия
                print(f"{threading.current_thread().name} завершается по таймеру")

    def run(self):
        self.make_work()


def task():
    print(f"{threading.current_thread().name} ВЫЗЫВАЕТ ЗАДАЧУ task!")


_count = count(1)


# допишите функцию permission
def permission():
    n = next(_count)
    thread_name = threading.current_thread().name
    print(f"{thread_name} проверяет предикат, permission вызывается {n}-й раз")
    return n == len(threading.enumerate()) + 2


# alt

def permission():
    n = next(_count)
    thread_name = threading.current_thread().name
    print(f"{thread_name} проверяет предикат, permission вызывается {n}-й раз")
    if n == 2:
        threading.current_thread().my_custom_flag = True
        return False
    return hasattr(threading.current_thread(), "my_custom_flag")
