import threading
from collections.abc import Generator
from queue import Queue


def get_obj() -> Generator:
    pass


def handler(elem):
    pass


queue = Queue()


def producer(queue, generator):
    for elem in generator():
        queue.put(elem)
    queue.put(None)


def consumer(queue):
    while True:
        elem = queue.get()
        if not elem:
            queue.put(elem)
            return
        handler(elem)


producer_thread = threading.Thread(target=producer, args=[queue, get_obj], name='producer', daemon=True)
producer_thread.start()

consumer_threads = [
    threading.Thread(target=consumer, args=[queue], name=f'consumer_{i}', daemon=True)
    for i in range(1, 3)
]
for thread in consumer_threads:
    thread.start()
for thread in consumer_threads:
    thread.join()
