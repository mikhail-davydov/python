import threading

lock = threading.Lock()


def task():
    with lock:
        some_work_part1()
        some_work_part2()
        some_work_part3()


# alt

def task():
    try:
        lock.acquire()
        some_work_part1()
        some_work_part2()
        some_work_part3()
    finally:
        lock.release()
