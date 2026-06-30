import threading

event = threading.Event()


def task():
    some_work_part1()
    some_work_part2()
    event.wait()
    some_work_part3()
