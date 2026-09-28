from asyncio import Queue

import asyncio
import inspect
from typing import Coroutine


class AsCompletedIterator:
    def __init__(self, coroutines):
        """
        Создаем список задач на основе переданного списка корутин.
        Назначаем коллбэк задачам
        Создаем очередь готовых задач asyncio.Queue(). Очередь создается пустая.

        :param coroutines: список объектов корутин
        """
        self._done = Queue()
        self._tasks = [asyncio.create_task(coro) for coro in coroutines]
        for task_ in self._tasks:
            task_.add_done_callback(self.callback_func)
        self._todo_left = len(self._tasks)

    def callback_func(self, task: asyncio.Task):
        """
        функция коллбэка, в которой готовая задача помещается в очередь готовых задач put_nowait(task)
        и эта задача удаляется из списка задач

        :param task: выполенная задача
        :return: None
        """
        self._done.put_nowait(task)
        self._tasks.remove(task)

    def __aiter__(self):
        return self

    async def __anext__(self):
        """
        если список задач пустой, возбуждаем исключение об окончании асинхронной итерации
        ожидаем завершенную задачу - элемент из очереди готовых задач get()
        и возвращаем его

        :return: готовую задачу из очереди
        """
        if not self._todo_left:
            raise StopAsyncIteration
        self._todo_left -= 1
        return await self._done.get()


def async_for_completed(aws: list[Coroutine]):
    """
    если aws не является списком из объектов корутин, возбуждаем исключение
    TypeError("Должен быть передан список с объектами корутин")
    возвращаем экземпляр класса <ИмяКласса>(aws)

    :param aws: список awaitable объектов
    :return: объект класса AsCompletedIterator
    """
    if not isinstance(aws, list):
        raise TypeError("Должен быть передан список с объектами корутин")
    for aw in aws:
        if not inspect.iscoroutine(aw):
            raise TypeError("Должен быть передан список с объектами корутин")

    return AsCompletedIterator(aws)
