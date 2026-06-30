from collections.abc import Callable
from threading import Timer, Thread


def check_main(main: Thread):
    print('target ВЫПОЛНЯЕТСЯ') if main.is_alive() else print('target ЗАВЕРШЕН')


def timeout_watchdog(target: Callable, timeout: float) -> None:
    """
    Запускает задачу target в фоне. Через timeout сообщает о ее состоянии.
    """
    main = Thread(target=target, daemon=True)
    main.start()

    timer = Timer(function=check_main, interval=timeout, args=[main])
    timer.start()


# alt

def timeout_watchdog(target: Callable, timeout: float) -> None:
    """
    Запускает задачу target в фоне. Через timeout сообщает о ее состоянии.
    """

    th1 = Thread(target=target, daemon=True)
    th1.start()

    def _check():
        if th1.is_alive():
            print("target ВЫПОЛНЯЕТСЯ")
        else:
            print("target ЗАВЕРШЕН")

    th2 = Timer(interval=timeout, function=_check)
    th2.start()
