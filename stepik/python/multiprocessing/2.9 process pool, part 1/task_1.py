from multiprocessing import Process

import multiprocessing
import os
from collections.abc import Iterable, Callable


def pool(max_workers: int = None, task: Callable = None, args: Iterable = None) -> None:
    max_workers = min(len(args or ()), max_workers or os.cpu_count())
    args_dict = {}
    for i, arg in enumerate(args):
        args_dict.setdefault(i % max_workers, []).append(arg)
    processes = [Process(target=worker, args=(task, args_value)) for args_value in args_dict.values()]
    for process in processes:
        process.start()
    for process in processes:
        process.join()


def worker(task: Callable, args: Iterable) -> None:
    for arg in args:
        task(arg)


def task(arg):
    print(f"ident={multiprocessing.current_process().ident}, {arg}")


if __name__ == "__main__":
    args = [1, 2, 3, 4, 5, 6, 7]
    pool(max_workers=3, task=task, args=args)


# alt

import multiprocessing


def tmp_task(task, args):
    for arg in args:
        task(arg)


def pool(max_workers=None, task=None, args=None):
    max_workers = max_workers or multiprocessing.cpu_count()
    n, nl = divmod(len(args), max_workers)
    parts = []
    process = []
    i = 0
    for j in range(max_workers):
        part_size = n + 1 if j < nl else n
        parts.append((args[i:i + part_size]))
        i += part_size
    for part in parts:
        if part:
            pr = multiprocessing.Process(target=tmp_task, args=(task, part))
            process.append(pr)
            pr.start()
    for pr in process:
        pr.join()