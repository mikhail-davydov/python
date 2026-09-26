import sys
import threading
import traceback
from traceback import StackSummary
from types import TracebackType


def custom_hook(args):
    exc_type, exc_value, exc_tb, exc_thread = args
    exc_tb: TracebackType
    exc_thread: threading.Thread

    original_output = sys.stdout
    sys.stdout = sys.stderr

    print(f'Exception in thread {exc_thread.name}:')

    stack_summary: StackSummary = traceback.extract_tb(exc_tb.tb_next.tb_next)
    function_names = [frame.name for frame in stack_summary]
    print(f'Traceback (only {len(function_names)} last call):')
    print(' -> '.join(function_names))
    print(f'{exc_type.__name__}: {exc_value}')

    sys.stdout = original_output


# alt
# def custom_hook(args):
#     thread_name = args.thread.name
#     print(f"Exception in thread {thread_name}:", file=sys.stderr)
#
#     frames = []
#     tb = args.exc_traceback
#     while tb:
#         frames.append(tb)
#         tb = tb.tb_next
#     user_frames = frames[2:]
#     depth = len(user_frames)
#     print(f"Traceback (only {depth} last call):", file=sys.stderr)
#
#     func_names = [tb.tb_frame.f_code.co_name for tb in user_frames]
#     print(" -> ".join(func_names), file=sys.stderr)
#
#     print(f"{args.exc_type.__name__}: {args.exc_value}", file=sys.stderr)


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
        # threading.Thread(target=raise_value_error),
        # threading.Thread(target=raise_runtime_error),
    ]

    for thread in threads:
        thread.start()
        thread.join()

    print('Done!')
