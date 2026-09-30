from typing import Any, AsyncIterator


async def json_gen() -> AsyncIterator[int]:
    item = iter(range(1, 11))
    while True:
        try:
            yield next(item)
        except StopIteration:
            break


async def registrator(elem: int) -> None:
    await asyncio.sleep(0)
    print(f'{elem} зарегистрирован для дальнейшей обработки')


def final() -> None:
    print('Final')


#####################################################################
#                              Your code

import asyncio
from asyncio import Event

event = Event()


async def producer(queue: asyncio.LifoQueue):
    async for elem in json_gen():
        await queue.put(elem)


async def consumer(queue: asyncio.LifoQueue):
    while not event.is_set():
        elem = await queue.get()
        await registrator(elem)
        queue.task_done()
        if queue.empty():
            event.set()


async def producer_consumer(queue: asyncio.LifoQueue):
    await asyncio.gather(producer(queue), consumer(queue), consumer(queue))
    await queue.join()
    final()


if __name__ == '__main__':
    queue: asyncio.LifoQueue[Any] = asyncio.LifoQueue()
    asyncio.run(producer_consumer(queue))
    print('End')


# alt
async def producer(queue: asyncio.LifoQueue):
    async for elem in json_gen():
        await queue.put(elem)
    event.set()


async def consumer(queue: asyncio.LifoQueue):
    while not event.is_set() or not queue.empty():
        elem = await queue.get()
        await registrator(elem)
        queue.task_done()


async def final_join(queue: asyncio.LifoQueue):
    await event.wait()
    await queue.join()
    final()


async def producer_consumer(queue: asyncio.LifoQueue):
    await asyncio.gather(producer(queue), consumer(queue), consumer(queue), final_join(queue))
