import threading
from collections.abc import Generator
from queue import Queue


def get_obj() -> Generator:
    pass


def handler(elem):
    pass


queue = Queue()


def producer():
    for elem in get_obj():
        queue.put(elem)


def consumer():
    while not queue.empty():
        try:
            handler(queue.get(block=False))
            # queue.task_done()
        except:
            pass


producer_thread = threading.Thread(target=producer, name='producer', daemon=True)
producer_thread.start()
producer_thread.join()

consumer_threads = [threading.Thread(target=consumer, name=f'consumer_{i}', daemon=True) for i in range(1, 3)]
for thread in consumer_threads:
    thread.start()
for thread in consumer_threads:
    thread.join()


# alt


def produce(queue, generator):
    for elem in generator():
        queue.put(elem)


def consume(queue):
    while not queue.empty():
        handler(queue.get())


queue = Queue()

producer = threading.Thread(target=produce, args=(queue, get_obj), name="producer")
producer.start()
producer.join()

consumer1 = threading.Thread(target=consume, args=(queue,), name="consumer_1")
consumer2 = threading.Thread(target=consume, args=(queue,), name="consumer_2")

consumer1.start()
consumer2.start()

consumer1.join()
consumer2.join()
