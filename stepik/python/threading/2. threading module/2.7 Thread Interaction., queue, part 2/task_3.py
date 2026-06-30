import threading
from collections.abc import Generator, Callable
from queue import Queue


def get_obj() -> Generator:
    pass


def handler(elem):
    pass


CONSUMERS_COUNT = 2

queue = Queue()


def producer(queue: Queue, generator: Callable):
    for elem in generator():
        queue.put(elem)


def consumer(queue: Queue):
    while True:
        elem = queue.get()
        handler(elem)
        queue.task_done()


producer_thread = threading.Thread(target=producer, args=[queue, get_obj], name='producer', daemon=True)
producer_thread.start()

consumer_threads = [
    threading.Thread(target=consumer, args=[queue], name=f'consumer_{i + 1}', daemon=True)
    for i in range(CONSUMERS_COUNT)
]
for thread in consumer_threads:
    thread.start()

producer_thread.join()
queue.join()
