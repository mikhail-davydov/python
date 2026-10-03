from asyncio import Future

import asyncio
import collections


class SimpleEvent:
    def __init__(self):
        # создайте очередь ожидающих (очередь для футур), используя collections.deque
        # хотя можете обойтись и обычным списком

        self._waiting: collections.deque[Future] = collections.deque()

    async def wait(self):
        # создайте экземпляр футуры
        # поместите футуру в очередь ожидающих
        # попробуйте дождаться футуру
        # в финализаторе удалите футуру из очереди ожидающих

        loop = asyncio.get_running_loop()
        fut = loop.create_future()
        self._waiting.append(fut)
        try:
            await fut
        except Exception:
            self._waiting.remove(fut)

    def set(self):
        # 'освобождаем' все ожидающие футуры, назначая им результат, например None
        # для всех футур из очереди ожидающих назначаем результат, если, конечно, футура уже не завершена

        waiting = self._waiting.copy()
        self._waiting.clear()
        for fut in waiting:
            if not fut.done():
                fut.set_result(None)


# alt original

class SimpleEvent:
    def __init__(self):
        self._waiters = collections.deque()

    async def wait(self):
        future = asyncio.get_running_loop().create_future()
        self._waiters.append(future)
        try:
            await future
        finally:
            self._waiters.remove(future)

    def set(self):
        for fut in self._waiters:
            if not fut.done():
                fut.set_result(None)
