import threading


def custom_hook(args):
    exc_type, exc_value, exc_traceback, thread = args
    print(thread.name, exc_type.__name__, exc_value, sep=', ')
    # print(f"Тип исключения: {exc_type.__name__}")
    # print(f"Сообщение исключения: {exc_value}")
    # print(f"Номер потока: {thread.ident}")
    # print(f"Имя потока: {thread.name}")
    # print(f"Путь исключения:")
    # traceback.print_tb(exc_traceback)


threading.excepthook = custom_hook