import time


def task(arg):
    time.sleep(arg / 3)
    return arg + arg


# Ваше решение
from typing import Iterable, Callable
from multiprocessing.context import TimeoutError


def main(func: Callable, iterable: Iterable, timeout: int) -> list:
    with Pool(8) as pool:
        processes = [pool.apply_async(func, [arg]) for arg in iterable]
        results = []
        end = timeout + time.perf_counter()
        for process in processes:
            try:
                to_wait = max(end - time.perf_counter(), 0)
                results.append(process.get(to_wait))
            except TimeoutError as err:
                results.append(err.__class__.__name__)
        return results


if __name__ == '__main__':
    data = (1, 2, 12, 1, 1.5, 1.5, 2, 5)
    print(main(task, data, 1))

# alt

from multiprocessing.pool import Pool
from typing import Iterable, Callable
from time import sleep


def main(func: Callable, iterable: Iterable, timeout: int) -> list:
    with Pool() as pool:
        result = []
        for args in iterable:
            rez = pool.apply_async(func, (args,))
            result.append(rez)
        sleep(timeout)
        for i, rez in enumerate(result):
            if rez.ready():
                result[i] = rez.get()
            else:
                result[i] = "TimeoutError"
        return result
