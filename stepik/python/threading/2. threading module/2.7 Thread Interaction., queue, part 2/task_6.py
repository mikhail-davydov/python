import queue
import threading
from collections.abc import Generator, Callable


def get_next_declaration() -> Generator[dict]: ...
def handler(task) -> bool: ...
class CCD:
    def __init__(self, data: dict): ...


def add_declaration(task: CCD, main: queue.Queue, sub: queue.Queue):
    try:
        main.put_nowait(task)
    except queue.Full:
        sub.put(task)


def produce(generator: Callable, main: queue.Queue, sub: queue.Queue):
    for data in generator():
        if data is None:
            return
        task = CCD(data)
        add_declaration(task, main, sub)


def consume(main: queue.Queue):
    try:
        while True:
            task = main.get_nowait()
            if handler(task):
                main.task_done()
    except queue.Empty:
        return


main_queue = queue.PriorityQueue(maxsize=30)
sup_queue = queue.Queue()

CONSUMERS_COUNT = 3

producer = threading.Thread(target=produce, args=(get_next_declaration, main_queue, sup_queue))
producer.start()
producer.join()

consumers = [
    threading.Thread(target=consume, args=[main_queue], name=f'inspector_{i}', daemon=True)
    for i in range(1, CONSUMERS_COUNT + 1)
]
for consumer in consumers:
    consumer.start()
for consumer in consumers:
    consumer.join()

try:
    while True:
        main_queue.put_nowait(sup_queue.get_nowait())
except:
    pass
