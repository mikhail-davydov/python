import time
from random import uniform


def get_files():
    for file in ["logo.png", "bar.png", "phon.png", "box.png", "info.png", "front_logo.png"]:
        time.sleep(uniform(0.05, 0.1))
        yield file
    time.sleep(60)


def image_processing(file: str) -> str:
    time.sleep(uniform(0.5, 0.7))  # эмуляция работы
    return f"{file} processed successfully"


#  Ваше решение:
from multiprocessing import Queue


def producer(queue: Queue):
    for file in get_files():
        queue.put(file)


def consumer(queue: Queue, log_queue: Queue):
    try:
        while True:
            result = image_processing(queue.get(timeout=QUEUE_TIMEOUT * CONSUMER_COUNT))
            print(result)
            log_queue.put(result)
    except Empty:
        pass


log_processing = []
CONSUMER_COUNT = 3
QUEUE_TIMEOUT = 0.1


def main():
    queue = Queue()
    log_queue = Queue()
    Process(target=producer, args=(queue,), daemon=True).start()

    processes = [Process(target=consumer, args=(queue, log_queue)) for _ in range(CONSUMER_COUNT)]

    for process in processes:
        process.start()
    for process in processes:
        process.join()

    try:
        while True:
            log_processing.append(log_queue.get_nowait())
    except Empty:
        pass


if __name__ == '__main__':
    main()
    print(log_processing)

# alt

from multiprocessing import Queue, Process, Manager
from queue import Empty
from multiprocessing.managers import SyncManager

def producer(queue) -> None:
    for file in get_files():
        queue.put(file)
    queue.close()

def consumer(queue: Queue, log_processing: SyncManager.list) -> None:
    try:
        while file:= queue.get(timeout=0.3):
            log = image_processing(file)
            log_processing.append(log)
    except Empty:
        queue.close()

if __name__ == '__main__':
    queue = Queue()

    sync_manager: SyncManager = Manager()
    log_processing = sync_manager.list()

    process_producer = Process(target=producer, args=(queue, ), daemon=True)
    processes_consumer = [Process(target=consumer, args=(queue, log_processing)) for _ in range(3)]

    process_producer.start()
    for process in processes_consumer:
        process.start()

    for process in processes_consumer:
        process.join()

    print(log_processing)
