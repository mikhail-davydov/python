import queue
import threading


def handler(elem):
    raise NotImplementedError


def logging_escape():
    raise NotImplementedError


tmp_queue = queue.Queue()

CONSUMERS_COUNT = 2


def consume():
    try:
        while True:
            handler(tmp_queue.get(timeout=0.1 * CONSUMERS_COUNT))
    except queue.Empty:
        logging_escape()


consumers = [
    threading.Thread(target=consume, name=f'consumer_{i + 1}', daemon=True)
    for i in range(CONSUMERS_COUNT)
]

for consumer in consumers:
    consumer.start()
for consumer in consumers:
    consumer.join()
