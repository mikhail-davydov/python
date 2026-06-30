import random
import threading
import time
from collections.abc import Callable


def finalizer():
    print("STAGE #1 ALL DONE!")


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

# alt

import threading


class ThrTask(threading.Thread):

    def __init__(self, name, barrier, task_stage1, task_stage2):
        super().__init__()
        self.name = name
        self.barrier = barrier
        self.task_stage1 = task_stage1
        self.task_stage2 = task_stage2

    def run(self):
        self.task_stage1()
        self.barrier.wait()
        self.task_stage2()

    @classmethod
    def make_thread(cls, name, **params):
        return cls(
            name=name,
            barrier=params['barrier'],
            task_stage1=params['task_stage1'],
            task_stage2=params['task_stage2'],
        )


barrier = threading.Barrier(4, action=finalizer)
params = {
    'barrier': barrier,
    'task_stage1': task_stage1,
    'task_stage2': task_stage2,
}

threads = [
    ThrTask.make_thread(name='Thread #1', **params),
    ThrTask.make_thread(name='Thread #2', **params),
    ThrTask.make_thread(name='Thread #3', **params),
    ThrTask.make_thread(name='Thread #4', **params),
]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
   