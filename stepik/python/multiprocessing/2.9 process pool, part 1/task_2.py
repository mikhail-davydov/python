from multiprocessing import Process, Queue

import time
from random import uniform


class SimplePool:
    def __init__(self, max_workers=None):
        self.max_workers = max_workers or multiprocessing.cpu_count()

    def map(self, task=None, args=None):
        if args is None:
            return []

        max_workers = min(len(args), self.max_workers)
        if max_workers == 0:
            return []

        # Распределение аргументов между процессами
        args_dict = {}
        for i, arg in enumerate(args):
            args_dict.setdefault(i % max_workers, []).append(arg)

        # Создание очереди для получения результатов
        result_queue = Queue()

        # Создание и запуск процессов
        processes = []
        for args_value in args_dict.values():
            p = Process(target=self._worker, args=(task, args_value, result_queue))
            processes.append(p)
            p.start()

        # Ожидание завершения всех процессов
        for p in processes:
            p.join()

        # Сбор результатов
        results = []
        while not result_queue.empty():
            results.append(result_queue.get())

        # Сортировка результатов по индексу (чтобы сохранить порядок)
        results.sort(key=lambda x: x[0])

        # Извлечение только значений результатов
        return [result[1] for result in results]

    def _worker(self, task, args, result_queue):
        for idx, arg in enumerate(args):
            result = task(arg)
            result_queue.put((idx, result))


def task(arg):
    time.sleep(uniform(0, 1))
    return multiprocessing.current_process().ident, arg


if __name__ == "__main__":
    args = [3, 2, 1, 5, 6, 7, 4]
    my_pool = SimplePool(3)
    for _id, v in my_pool.map(task=task, args=args):
        print(f"ident={_id}, {v}")

# alt

import multiprocessing
from typing import Callable


class SimplePool():
    def __init__(self, max_workers=None):
        if max_workers is None:
            max_workers = multiprocessing.cpu_count()
        assert isinstance(max_workers, int) and max_workers >= 1
        self.max_workers = max_workers
        self._q = multiprocessing.Queue()

    @staticmethod
    def _tmp_task(task, args, q):
        for arg in args:
            q.put({arg: task(arg)})

    def map(self, task: Callable = None, args: tuple = None):
        n, nl = divmod(len(args), self.max_workers)
        parts = []
        process = []
        result = {}
        i = 0
        for j in range(self.max_workers):
            part_size = n + 1 if j < nl else n
            parts.append((args[i:i + part_size]))
            i += part_size
        for part in parts:
            if part:
                pr = multiprocessing.Process(target=self._tmp_task, args=(task, part, self._q))
                process.append(pr)
                pr.start()
        for pr in process:
            pr.join()
        while not self._q.empty():
            result.update(self._q.get())
        return [result[ar] for ar in args]
