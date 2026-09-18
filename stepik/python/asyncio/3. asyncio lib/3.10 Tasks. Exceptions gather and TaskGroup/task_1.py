import asyncio


def cb(task: asyncio.Task):
    try:
        all_results[task.get_name()] = task.exception() or task.result()
    except asyncio.CancelledError as error:
        all_results[task.get_name()] = error


async def main():
    tasks = [
        asyncio.create_task(coro, name=f'Task_{coro.__name__}')
        for coro in coroutines
    ]
    for task in tasks:
        task.add_done_callback(cb)
    for task in tasks:
        try:
            await task
        except BaseException:
            pass


if __name__ == '__main__':
    all_results = {}
    asyncio.run(main())

coroutines = []


# alt


def cb(task: asyncio.Task) -> None:
    coro_name = task.get_coro().__name__
    try:
        all_results[f'Task_{coro_name}'] = task.result()
    except BaseException as error:
        all_results[f'Task_{coro_name}'] = error


async def main():
    tasks = [asyncio.create_task(coro) for coro in coroutines]
    for task in tasks:
        task.add_done_callback(cb)
    await asyncio.gather(*tasks, return_exceptions=True)


# alt

async def main():
    tasks = [asyncio.create_task(coro, name=f"Task_{coro.__name__}") for coro in coroutines]
    await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

    for task in tasks:
        try:
            result = task.result()
            all_results[task.get_name()] = result
        except Exception as e:
            all_results[task.get_name()] = e
        except BaseException as e:
            all_results[task.get_name()] = e
