import threading

[print(thread.name) for thread in threading.enumerate() if thread is not threading.main_thread()]
