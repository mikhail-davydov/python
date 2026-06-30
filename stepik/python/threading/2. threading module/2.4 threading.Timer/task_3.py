import threading


def executer():
    pass


def logging():
    pass


def test_thread_timer(t_check: int | float):
    main = threading.Thread(target=executer, daemon=True, name='Thread')
    timer = threading.Timer(interval=t_check + 0.01, function=logging)
    timer.name = 'Timer'

    main.start()
    timer.start()

    main.join(t_check)
    if not main.is_alive():
        timer.cancel()
