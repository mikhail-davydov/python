import asyncio
import time
from typing import Callable, Coroutine


class TaskGroupCB:
    def __init__(self, cb: Callable = None):
        self._cb = cb
        self._tasks = []

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await asyncio.gather(*self._tasks)
        self._tasks.clear()

    def create_task(self, coro: Coroutine, *, name=None):
        task = asyncio.create_task(coro, name=name)
        task.add_done_callback(self._cb)
        self._tasks.append(task)


async def coro(i):
    return await asyncio.sleep(i / 10, i)


def callback(task: asyncio.Task):
    print(f"Задача {task.get_name()} завершилась успешно с результатом {task.result()}")


async def main():
    async with TaskGroupCB(callback) as tgc:
        for n in range(10):
            tgc.create_task(coro(n), name=f"task#{n}")


if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(main())
    print(f"\nAll done in {time.perf_counter() - start_time:.2f}с.")


# alt


class TaskGroupCB:
    def __init__(self, cb: callable):
        self._tasks = set()
        self._cb = cb

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await asyncio.gather(*self._tasks)

    def create_task(self, coro, *, name=None):
        task = asyncio.create_task(coro, name=name)
        if task.done():
            self._tasks.discard(task)
        else:
            self._tasks.add(task)
            task.add_done_callback(lambda _: self._tasks.discard(task))
        task.add_done_callback(self._cb)
        return task


# alt


class TaskGroupCB:
    def __init__(self, callback: Callable):
        self._callback = callback
        self._tasks = set()
        self._all_complete_future: asyncio.Future | None = None

    async def __aenter__(self):
        return self

    def _cleanup_task(self, task: asyncio.Task):
        self._tasks.remove(task)

        if not self._tasks and self._all_complete_future and not self._all_complete_future.done():
            self._all_complete_future.set_result("Finished")

    def create_task(self, coro, *, name: str | None = None):
        task = asyncio.create_task(coro, name=name)
        task.add_done_callback(self._callback)
        task.add_done_callback(self._cleanup_task)
        self._tasks.add(task)
        return task

    async def __aexit__(self, exc_type, exc_value, traceback):
        while self._tasks:
            if not self._all_complete_future:
                loop = asyncio.get_running_loop()
                self._all_complete_future = loop.create_future()
            await self._all_complete_future
