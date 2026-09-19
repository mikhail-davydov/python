import asyncio


async def wait_tasks(tasks: list[asyncio.Task], timeout: float | int) -> tuple[dict, set]:
    done, not_done_tasks = await asyncio.wait(tasks, timeout=timeout)
    done: set[asyncio.Task]
    results = {}
    for task in done:
        try:
            results[task.get_name()] = task.result()
        except asyncio.CancelledError:
            results[task.get_name()] = 'Cancelled'
        except Exception:
            results[task.get_name()] = task.exception()
    return results, not_done_tasks


# alt

async def wait_tasks(tasks: list[asyncio.Task], timeout: float | int) -> tuple[dict, set]:
    done, pending = await asyncio.wait(tasks, timeout=timeout)
    res = {t.get_name(): "Cancelled" if t.cancelled() else t.exception() or t.result() for t in done}
    return res, pending


# alt

async def wait_tasks(tasks: list[asyncio.Task], timeout: float | int) -> tuple[dict, set]:
    results = {}
    done, not_done = await asyncio.wait(tasks, timeout=timeout)
    for task in done:
        if task.cancelled():
            results[task.get_name()] = "Cancelled"
        elif ex := task.exception():
            results[task.get_name()] = ex
        else:
            results[task.get_name()] = task.result()
    return results, not_done
