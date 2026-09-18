from asyncio import CancelledError

import asyncio


def cb(task: asyncio.Task) -> None:
    coro_name = task.get_coro().__name__
    try:
        if task.exception():
            print(f"Задача с корутиной {coro_name} завершилась с исключением {task.exception()!r}")
        if task.result():
            print(f"Задача с корутиной {coro_name} вернула результат {task.result()}")
    except CancelledError:
        print(f'Задача с корутиной {coro_name} завершилась с исключением CancelledError()')
    except Exception:
        pass


# alt

def cb(task: asyncio.Task) -> None:
    coro_name = task.get_coro().__name__
    try:
        print(f"Задача с корутиной {coro_name} вернула результат {task.result()}")
    except BaseException as error:
        print(f"Задача с корутиной {coro_name} завершилась с исключением {repr(error)}")
