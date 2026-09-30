from time import perf_counter
from typing import Any

type T = dict[str, list[Any]]

start = perf_counter()


async def scrap() -> T:
    while perf_counter() - start < 3:
        return {}
    return {'new': ["товар№1", "товар№2", "товар№3", "товар№4", "товар№5"]}


async def spider(item: Any) -> None:
    print(f'{item} is caught')


#########################Your code #####################################

import asyncio
from asyncio import Event, Queue

event = Event()
queue = Queue()

ITEMS_KEY = 'new'
SPIDERS_COUNT = 5


async def coro_watcher():
    print('Start watcher')
    while not event.is_set():
        await asyncio.sleep(0.1)
        items = await scrap()
        if ITEMS_KEY in items:
            [queue.put_nowait(item) for item in items[ITEMS_KEY]]
            event.set()


async def coro_handler():
    print('Start handler')
    await event.wait()
    item = await queue.get()
    await spider(item)


async def main_logic():
    handlers = [coro_handler() for _ in range(SPIDERS_COUNT)]
    await asyncio.gather(coro_watcher(), *handlers)


if __name__ == '__main__':
    asyncio.run(main_logic())

# alt
new_products = []


async def coro_watcher():
    global new_products
    while True:
        await asyncio.sleep(0.1)
        info: dict = await scrap()
        if v := info.get("new"):
            new_products = v
            event.set()
            break


async def coro_handler(index: int):
    await event.wait()
    await spider(new_products[index])


async def main_logic():
    await asyncio.gather(coro_watcher(), *(coro_handler(index) for index in range(5)))
