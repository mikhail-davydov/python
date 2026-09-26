import threading


def custom_exception_handler(args):
    current = threading.current_thread()
    if current.daemon:
        print(current.name)


threading.excepthook = custom_exception_handler


# alt

def custom_hook(args):
    exc_type, exc_value, exc_traceback, thread = args
    if thread.daemon:
        print(thread.name)
