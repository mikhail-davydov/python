import time
from random import uniform


def get_files():
    for file in ["logo.png", "bar.png", "phon.png", "box.png", "info.png", "front_logo.png"]:
        time.sleep(uniform(0.05, 0.1))
        yield file
    yield None


def image_processing(file: str) -> str:
    time.sleep(uniform(0.5, 0.7))  # эмуляция работы
    return f"{file} processed successfully"


#  Ваше решение:
from multiprocessing import Queue


def producer(queue: Queue):
    for file in get_files():
        queue.put(file)


def consumer(queue: Queue, log_queue: Queue):
    while True:
        elem = queue.get()
        if elem is None:
            queue.put(elem)
            return

        result = image_processing(elem)
        print(result)
        log_queue.put(result)


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

    while not log_queue.empty():
        log_processing.append(log_queue.get_nowait())


if __name__ == '__main__':
    main()
    print(log_processing)


# alt

from multiprocessing import Queue, Process, Manager

def add_to_queue(queue_work):
    for file in get_files():
        queue_work.put(file)

def borshov_an(queue_work, borshov_result):
    while file := queue_work.get():
        work = image_processing(file)
        borshov_result.append(work)
    queue_work.put(None)

def main():
    Process(target=add_to_queue, args=(queue_work,), daemon=True).start()
    processes = [Process(target=borshov_an, args=(queue_work, log_processing,))
                 for _ in range(3)]
    [process.start() for process in processes]
    [process.join() for process in processes]

if __name__ == '__main__':
    queue_work = Queue()
    sync_manager = Manager()
    log_processing = sync_manager.list()
    main()