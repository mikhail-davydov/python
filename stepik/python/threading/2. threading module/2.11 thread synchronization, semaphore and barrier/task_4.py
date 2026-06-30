import random
import threading
import time
from collections.abc import Callable


def shutdown():
    print(f"ALL DONE! by {threading.current_thread().name}")


def finalizer():
    print(f"STAGE DONE! by {threading.current_thread().name}")


def task_stage1():
    time.sleep(random.uniform(0, 1))
    print(f"stage #1 done by {threading.current_thread().name}")


def task_stage2():
    time.sleep(random.uniform(0, 1))
    print(f"stage #2 done by {threading.current_thread().name}")


def target(barrier: threading.Barrier, task_1: Callable, task_2: Callable):
    task_1()
    barrier.wait()
    task_2()
    if barrier.wait() == 0:
        shutdown()


barrier = threading.Barrier(parties=4, action=finalizer)

threads = [
    threading.Thread(
        target=target,
        args=(barrier, task_stage1, task_stage2),
        name=f'Thread #{i}',
    )
    for i in range(1, 5)
]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
