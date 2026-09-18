import asyncio
from functools import partial


async def main():
    async with asyncio.TaskGroup() as tg:
        for coro, cb, arg in zip(coroutines, callbacks, arguments):
            task = tg.create_task(coro(arg), name=coro.__name__)
            task.add_done_callback(partial(cb, arg))


if __name__ == '__main__':
    asyncio.run(main())

coroutines = []
callbacks = []
arguments = []


# alt

async def main():
    async with asyncio.TaskGroup() as tg:
        for cb, coro, arg in zip(callbacks, coroutines, arguments):
            tg.create_task(coro(arg), name=coro.__name__).add_done_callback(partial(cb, arg))
