import threading


def test():
    print('task done!')

test_thread = threading.Thread(target=test)
test_thread.start()
test_thread.join()