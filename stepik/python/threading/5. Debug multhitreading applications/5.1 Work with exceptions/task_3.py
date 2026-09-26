import threading


def custom_hook(args):
    exc_type, exc_value, exc_traceback, thread = args
    thread: threading.Thread
    prefix = 'Демонический поток' if thread.daemon else 'Поток'
    print(f'{prefix} {thread.name} завершился с ошибкой {exc_value!r}')


threading.excepthook = custom_hook
