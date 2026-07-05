import multiprocessing
from typing import Callable


def task():
    print("Вызвана целевая задача...")


def print_process_info(func: Callable):
    current = multiprocessing.current_process()
    parent = multiprocessing.parent_process()
    print(f'Процесс: {current.name}, PID={current.pid}, daemon={current.daemon}')
    print(f'Родительский процесс: {parent.name}, PID={parent.pid}')
    print(f'Целевая задача процесса: {func.__name__}')
    print(f'Вызвана целевая задача {func.__name__}...')


if __name__ == '__main__':
    pr = multiprocessing.Process(target=print_process_info, args=[task])
    pr.start()
    pr.join()
