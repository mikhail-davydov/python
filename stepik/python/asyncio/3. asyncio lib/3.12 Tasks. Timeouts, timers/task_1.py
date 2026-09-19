import asyncio


async def main(coroutines) -> list[str]:
    try:
        async with asyncio.timeout(None) as t:
            tasks = [asyncio.create_task(coro) for coro in coroutines]
            response_limit_task = [task for task in tasks if task.get_coro().__name__ == 'response_limit'].pop()
            timeout = await response_limit_task
            t.reschedule(asyncio.get_running_loop().time() + timeout)
            for task in tasks:
                await task
    except TimeoutError:
        pass

    return [
        task.get_coro().__name__
        for task in tasks
        if task.done() and not task.cancelled() and task.get_coro().__name__ != 'response_limit'
    ]


# alt

async def main(coroutines):
    try:
        async with asyncio.timeout(None) as atm:
            tasks = {coro.__name__: asyncio.create_task(coro) for coro in coroutines}
            delay = await tasks.pop('response_limit')
            atm.reschedule(asyncio.get_running_loop().time() + delay)
            await asyncio.wait(*tasks.values())
    except TimeoutError:
        pass
    return [coro_name for coro_name, task in tasks.items() if not task.cancelled()]