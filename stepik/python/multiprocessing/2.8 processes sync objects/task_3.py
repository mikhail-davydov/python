def handler(elem):
    ...


from multiprocessing import Queue, Semaphore


def worker(elem_queue: Queue, result_queue: Queue, obj_lock: Semaphore) -> None:
    while not elem_queue.empty():
        elem = elem_queue.get()
        with obj_lock:
            result_queue.put(handler(elem))


if __name__ == "__main__":
    elem_queue = Queue()
    result_queue = Queue()
    obj_lock = Semaphore(3)
