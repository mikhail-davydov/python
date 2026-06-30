import threading
import traceback


def custom_excepthook(args):
    """
    Обработчик неперехваченных исключений в потоках.
    Создает файл <thread_name>.txt с трейсбеком и информацией об ошибке.
    """
    thread = args.thread
    exc_type = args.exc_type
    exc_value = args.exc_value
    exc_traceback = args.exc_traceback

    # Получаем имя потока
    thread_name = thread.name

    # Формируем трейсбек в виде строки вызовов
    tb_lines = traceback.extract_tb(exc_traceback)
    function_names = []

    # Фильтруем внутренние вызовы threading и собираем только пользовательские
    for frame in tb_lines:
        # Пропускаем внутренние вызовы threading
        if 'threading' in frame.filename or frame.name in ('_bootstrap_inner', 'run'):
            continue
        function_names.append(frame.name)

    # Записываем в файл
    filename = f"{thread_name}.txt"
    with open(filename, 'w') as f:
        f.write("Traceback:\n")
        f.write(" -> ".join(function_names))
        f.write("\nException:\n")
        f.write(f"{exc_type.__name__}: {exc_value}")


# Переопределяем threading.excepthook
threading.excepthook = custom_excepthook

# alt

import threading


def custom_hook(args):
    exc_type, exc_value, exc_traceback, exc_thread = args
    path_tr = []
    while exc_traceback:
        name = exc_traceback.tb_frame.f_code.co_name
        path_tr.append(name)
        exc_traceback = exc_traceback.tb_next
    file_name = f"{exc_thread.name}.txt"
    with open(file_name, "w") as file:
        file.write(f"Traceback:\n{' -> '.join(path_tr[2:])}\nException:\n{exc_type.__name__}: {exc_value}")


threading.excepthook = custom_hook
