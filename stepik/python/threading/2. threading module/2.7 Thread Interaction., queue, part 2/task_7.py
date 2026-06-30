import queue
import threading
from datetime import datetime

def handler(task) -> bool: ...
main_queue = queue.PriorityQueue(maxsize=30)


def consumer(t_wait: float) -> None:
    name = threading.current_thread().name
    while True:
        try:
            task = main_queue.get(timeout=t_wait)
            print(f'Декларация с id = {task.id} поручена инспектору {name}')
            handler(task)
        except queue.Empty:
            now = datetime.now()
            print(f'Очередь пустая, {now}, инспектор {name} не занят')
