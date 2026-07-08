from string import ascii_lowercase

import random
import sys
from time import sleep


def get_obj():
    for _ in range(1, 12):
        sleep_time = random.uniform(0.0, 0.35)
        arr = ''.join(map(str, [random.randint(1, 9) for _ in range(3)]))
        row = ''.join([ascii_lowercase[int(arr[0])], ascii_lowercase[int(arr[1])], ascii_lowercase[int(arr[-1])]])
        yield (sleep_time, int(arr), row)


def worker(arg):
    print(f'sleeping: {round(arg[0], 3)} ...')
    sys.stdout.flush()
    sleep(arg[0])
    return arg[-1], arg[1], arg[0]


from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection


def child_process(conn: Connection):
    while conn.poll(timeout=None):
        result = worker(conn.recv())
        conn.send(result)


if __name__ == '__main__':
    main_conn, child_conn = Pipe()
    main_conn: Connection
    child_conn: Connection
    Process(target=child_process, args=[child_conn], daemon=True).start()

    for obj in get_obj():
        main_conn.send(obj)

    result = []
    while main_conn.poll(0.3):
        result.append(main_conn.recv())

    print(result)
