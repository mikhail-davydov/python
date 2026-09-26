import sys
import threading
import traceback

FRAMES_TO_SHOW = 2


def custom_hook(args):
    exc_type, exc_value, exc_tb, exc_thread = args
    exc_thread: threading.Thread

    print(f'Exception in thread {exc_thread.name}, daemon={exc_thread.daemon}, ID={exc_thread.native_id}:', file=sys.stderr)
    print(f'Traceback (only {FRAMES_TO_SHOW} last call):', file=sys.stderr)
    traceback.print_tb(exc_tb, limit=-FRAMES_TO_SHOW)
    print(f'{exc_type.__name__}: {exc_value}', file=sys.stderr)


# alt
# def custom_hook(args: threading.ExceptHookArgs):
#     header = (f"Exception in thread {args.thread.name}, "
#               f"daemon={args.thread.daemon}, "
#               f"ID={args.thread.native_id}:\n")
#     lines = traceback.format_exception(args.exc_type, value=args.exc_value, limit=-2, tb=args.exc_traceback)
#     lines[0] = "Traceback (only 2 last call):\n"
#     print(header, *lines, sep="", file=sys.stderr)


threading.excepthook = custom_hook


def raise_type_error():
    raise TypeError('type error exception')


def raise_value_error():
    raise ValueError('value error exception')


def raise_runtime_error():
    raise RuntimeError('runtime error exception')


if __name__ == '__main__':
    threads = [
        threading.Thread(target=raise_type_error),
        threading.Thread(target=raise_value_error),
        threading.Thread(target=raise_runtime_error),
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print('Done!')
