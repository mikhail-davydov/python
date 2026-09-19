import asyncio


def handler(task: asyncio.Task):
    if task.cancelled():
        cancelled.append(task.get_coro().__name__)
    else:
        if error := task.exception():
            results.append(error)
        else:
            results.append(task.result())


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            for coro in coroutines:
                tg.create_task(coro).add_done_callback(handler)
    except Exception as ex:
        pass


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
        results.append(err if (err := task.exception()) else task.result())
