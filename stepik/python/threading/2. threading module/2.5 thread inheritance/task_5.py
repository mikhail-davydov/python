import threading


class NoTargetException(Exception):
    def __init__(self, thread_nane: str):
        print(f'{thread_nane} has no target')


class MyThread(threading.Thread):
    def __init__(self, target=None, result=None):
        super().__init__()
        self.target = target
        self.result = result

    def run(self):
        if not self.target:
            raise NoTargetException(self.name)
        self.result = self.target()


def custom_hook(args):
    exc_type, exc_value, exc_traceback, thread = args
    if isinstance(exc_type, NoTargetException):
        return
    print(f'{thread.name} (id={thread.ident}) failed')


threading.excepthook = custom_hook
