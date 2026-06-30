import threading
from typing import Callable


def thread_log(task: Callable, log_task: Callable, t_check: int | float) -> None:
    thread = threading.Thread(target=task, daemon=True)
    timer = threading.Timer(interval=t_check + 0.01, function=log_task)
    thread.start()
    timer.start()

    thread.join(t_check)
    if not thread.is_alive():
        timer.cancel()
