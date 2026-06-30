from concurrent.futures import ThreadPoolExecutor

import threading


def task(n: int):
    pass


def init():
    current = threading.current_thread().name
    print(f'Поток {current} выполняет инициализацию')


with ThreadPoolExecutor(max_workers=3, thread_name_prefix='task_pool', initializer=init) as pool:
    pool.map(task, range(1, 11))
