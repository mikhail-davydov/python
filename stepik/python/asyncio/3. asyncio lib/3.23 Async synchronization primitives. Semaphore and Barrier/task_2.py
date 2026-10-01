from asyncio import Semaphore

import asyncio
from typing import Callable


class AsyncHubHandler:
    def __init__(self, limit: int, coro_function: Callable, n_tasks: int):
        self._sema = Semaphore(limit)
        self._coro = coro_function
        self._n_tasks = n_tasks

    async def start_hub(self):
        # Создаем все задачи сразу.
        # Семафор внутри worker() обеспечит ограничение количества одновременных выполнений.
        tasks = [asyncio.create_task(self.worker()) for _ in range(self._n_tasks)]

        # Ждем завершения всех задач
        await asyncio.gather(*tasks)

    async def worker(self):
        async with self._sema:
            await self._coro()
