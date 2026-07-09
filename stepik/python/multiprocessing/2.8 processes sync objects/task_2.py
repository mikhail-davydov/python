def handler(elem):
    ...


from multiprocessing import Lock, SimpleQueue


def worker(lock: Lock, stor: SimpleQueue) -> None:
    while True:
        with lock:
            if elem := stor.get():
                stor.put(handler(elem))
            else:
                break
