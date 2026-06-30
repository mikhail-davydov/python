from collections.abc import Generator

from queue import Queue
from threading import Thread


def get_obj() -> Generator:
    pass


def handler(elem):
    pass


def is_valid(elem):
    pass


CONSUMERS_COUNT = 2

valid_queue = Queue()
none_valid_queue = Queue()


def main():
    for elem in get_obj():
        valid_queue.put(elem) if is_valid(elem) else none_valid_queue.put(elem)
    for _ in range(CONSUMERS_COUNT):
        valid_queue.put(None)


main_th = Thread(target=main)
main_th.start()


def task():
    while True:
        elem = valid_queue.get()
        if elem is None:
            return
        handler(elem)


threads = [Thread(target=task) for _ in range(CONSUMERS_COUNT)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
