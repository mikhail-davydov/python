import time
from random import uniform


def get_files():
    for file in ["logo.png", "bar.png", "phon.png", "box.png", "info.png", "front_logo.png"]:
        time.sleep(uniform(0.05, 0.1))
        yield file
    # time.sleep(60)


def image_processing(file: str) -> str:
    time.sleep(uniform(0.5, 0.7))  # эмуляция работы
    return f"{file} processed successfully"


#  Ваше решение:
from multiprocessing import Process, JoinableQueue, SimpleQueue


def producer(queue: JoinableQueue):
    for file in get_files():
        queue.put(file)


def consumer(queue: JoinableQueue, log_queue: SimpleQueue):
    while True:
        result = image_processing(queue.get())
        print(result)
        log_queue.put(result)
        queue.task_done()


CONSUMER_COUNT = 3


def main():
    queue = JoinableQueue()
    log_queue = SimpleQueue()
    producer_pr = Process(target=producer, args=(queue,), daemon=True)
    producer_pr.start()

    consumers = [Process(target=consumer, args=(queue, log_queue), daemon=True) for _ in range(CONSUMER_COUNT)]
    for consumer_pr in consumers:
        consumer_pr.start()

    producer_pr.join()
    queue.join()

    while not log_queue.empty():
        log_processing.append(log_queue.get())


if __name__ == '__main__':
    log_processing = []
    main()
    print(log_processing)
