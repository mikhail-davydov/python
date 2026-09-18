import asyncio


def handler(task: asyncio.Task) -> None:
    if task.cancelled():
        cancelled.append(task.get_coro().__name__)
    else:
        results.append(err if (err := task.exception()) else task.result())


async def main():
    last_coro = coroutines.pop()
    last_task = asyncio.create_task(last_coro)
    last_task.add_done_callback(handler)
    try:
        async with asyncio.TaskGroup() as tg:
            for coro in coroutines:
                tg.create_task(coro).add_done_callback(handler)
    except Exception as ex:
        pass
    await last_task


if __name__ == '__main__':
    results = []
    cancelled = []
    asyncio.run(main())

coroutines = []


# alt

def handler(task: asyncio.Task) -> None:
    if task.cancelled():
        cancelled.append(task.get_coro().__name__)
    else:
        results.append(task.exception() or task.result())
