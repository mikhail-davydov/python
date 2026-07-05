from concurrent.futures import ThreadPoolExecutor

import multiprocessing
import typing


def request_handler(requests: list[typing.Callable], sources: list[str], timeout: int | float) -> None:
    process = multiprocessing.Process(target=tasks_handler, args=[requests, sources], daemon=True)
    process.start()
    process.join(timeout)

    if process.is_alive():
        process.terminate()
        process.join()
        process.close()


def tasks_handler(requests: list[typing.Callable], sources: list[str]):
    with ThreadPoolExecutor(max_workers=len(sources)) as pool:
        for request, source in zip(requests, sources):
            pool.submit(request, source)
