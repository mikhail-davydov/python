import asyncio


async def main():
    async with asyncio.TaskGroup() as tg:
        for coro, cb in zip(coroutines, callbacks):
            task = tg.create_task(coro, name=coro.__name__)
            task.name = task.get_name()
            task.add_done_callback(cb)


if __name__ == '__main__':
    asyncio.run(main())

coroutines = []
callbacks = []
