import threading


def test():
    pass

thread = threading.Thread(target=test, daemon=True)
thread.start()
thread.join(2)