from typing import Any

from types import FrameType

import threading
import time


def trace_func(frame, event, arg):
    thread_ = threading.current_thread()

    if event == 'call':
        print(f"{thread_.name} call {frame.f_code.co_name}")
    if event == 'return':
        print(f"{thread_.name} return {arg} for {frame.f_code.co_name}")

    return trace_func


threading.settrace(trace_func)


def dump_work():
    time.sleep(1)
    return 'some value'


thread = threading.Thread(target=dump_work, name='MyThread')
thread.start()

# alt

_thread_funcs = {}


def trace_func(frame: FrameType, event: str, arg: Any):
    thread_ = threading.current_thread()
    key = thread_.ident
    func_name = frame.f_code.co_name
    if event == "call":
        if func_name == "run":
            # начинаем следить за целевой функцией
            _thread_funcs[key] = None
            return None
        if key not in _thread_funcs or _thread_funcs[key] is not None:
            # если целевая функция завершена или её имя уже установлено, не мониторим ненужные нам функции
            return None
        if _thread_funcs[key] is None:
            # выставляем название целевой функции
            _thread_funcs[key] = func_name
    elif event == "return":
        if func_name == _thread_funcs.get(key):
            # очищаем словарь, чтобы не оставлять уже ненужные объекты в памяти
            # и не ломать логику при переиспользовании ID потока
            _thread_funcs.pop(key)
            print(thread_.name, func_name, arg)
    return trace_func
