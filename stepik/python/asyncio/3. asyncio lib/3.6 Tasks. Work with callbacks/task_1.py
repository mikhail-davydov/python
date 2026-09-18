import asyncio


async def main():
    async with asyncio.TaskGroup() as tg:
        for cb, coro in zip(callbacks, coroutines):
            tg.create_task(coro).add_done_callback(cb)


if __name__ == '__main__':
    asyncio.run(main())

coroutines = []
callbacks = []

# alt

async def main():
    tasks = []
    for coro, call in zip(coroutines, callbacks):
        task = asyncio.create_task(coro)
        task.add_done_callback(call)
        tasks.append(task)
    await asyncio.gather(*tasks)