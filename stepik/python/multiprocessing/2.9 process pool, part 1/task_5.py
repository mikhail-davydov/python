from multiprocessing.pool import Pool, AsyncResult
from typing import Iterable


def main(iterable: Iterable) -> None:
    with Pool() as pool:
        result: AsyncResult = pool.map_async(task, iterable, callback=handler, error_callback=err_handler)
        result.wait()


def task(): ...
def data_gen(): ...
def handler(): ...
def err_handler(): ...


if __name__ == '__main__':
    main(data_gen())
    ...


# alt

from multiprocessing.pool import Pool
from typing import Iterable


def main(iterable: Iterable) -> None:
    with Pool() as pool:
        result = pool.map_async(task, iterable, callback=handler, error_callback=err_handler)
        try:
            result.get()
        except Exception as err:
            pass


# alt

from multiprocessing.pool import Pool
from typing import Iterable


def main(iterable: Iterable) -> None:
    with Pool() as pool:
        futures = [pool.apply_async(task, (item,)) for item in iterable]
        try:
            results = [future.get() for future in futures]
            handler(results)
        except Exception as err:
            err_handler(err)