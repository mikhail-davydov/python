import threading


def custom_hook(args):
    exc_type, exc_value, exc_traceback, thread = args

    if exc_type == TypeError or exc_type == ValueError:
        print(f'{thread.name}, {exc_type.__name__}, {exc_value}')
    else:
        with open('custom_errors.txt', 'w', encoding='u8') as file:
            file.write(f'{thread.name}, {exc_type.__name__}, {exc_value}')


threading.excepthook = custom_hook


# alt

def custom_hook(args):
    exc_type, exc_value, exc_traceback, exc_thread = args
    output = sys.stdout if exc_type in (TypeError, ValueError) else open('custom_errors.txt', 'a+')
    print(f"{exc_thread.name}, {exc_type.__name__}, {exc_value}", file=output)
