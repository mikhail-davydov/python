import time


def task(i):
    time.sleep(i)
    if i == 1:
        raise ValueError("Ops, ValueError")
    return i


###
import multiprocessing


class WaitPool(object):
    def __init__(self, task, args):
        self._task = task
        self._args = args
        self._pool = multiprocessing.Pool()
        self._ap_rs = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._pool.terminate()

    def start(self):
        self._ap_rs = [self._pool.apply_async(func=task, args=[a]) for a in self._args]

    def wait(self):
        r_done, r_not_done = [], []
        for r in self._ap_rs:
            [r_not_done, r_done][r.ready() and r.successful()].append(r)

        return r_done, r_not_done


###

if __name__ == "__main__":
    args = (0.5, 1, 1.1, 2.2, 3.3, 1.2, 1.4)

    with WaitPool(task, args) as pool:
        pool.start()
        time.sleep(2)
        done, not_done = pool.wait()

    print(len(done), len(not_done))  # 4, 3

    for d in done:
        print(d.get())
    try:
        not_done[0].get()
    except ValueError as err:
        print(err)
