# импортируйте необходимое
import threading


def get_data():
    pass


def get_request():
    pass


def get_another_job():
    pass


# создайте объект семафора
semaphore = threading.Semaphore(2)


def semaphored_task():
    if semaphore.acquire(blocking=False):
        get_data()
        get_request()
        semaphore.release()
    else:
        get_another_job()
