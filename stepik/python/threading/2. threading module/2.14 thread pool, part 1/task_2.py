from concurrent.futures import ThreadPoolExecutor, TimeoutError

import threading


def task(n: int):
    current = threading.current_thread().name
    return f'Поток {current} выполнил задачу'


def init():
    current = threading.current_thread().name
    print(f'Поток {current} выполняет инициализацию')


with ThreadPoolExecutor(max_workers=3, thread_name_prefix='task_pool', initializer=init) as pool:
    try:
        results = pool.map(task, range(1, 11), timeout=1)
        for result in results:
            print(result)
    except TimeoutError:
        print('Завершение работы по таймауту!')
