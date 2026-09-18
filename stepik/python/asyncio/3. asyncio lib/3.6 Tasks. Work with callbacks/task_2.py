import asyncio


async def main():
    async with asyncio.TaskGroup() as tg:
        for cb, coro in zip(callbacks, coroutines):
            task = tg.create_task(coro)
            task.set_name(coro.__name__)
            task.add_done_callback(cb)


if __name__ == '__main__':
    asyncio.run(main())

coroutines = []
callbacks = []

# alt

async def main():
    async with asyncio.TaskGroup() as tg:
        for cb, coro in zip(callbacks, coroutines):
            tg.create_task(coro, name=coro.__name__).add_done_callback(cb)