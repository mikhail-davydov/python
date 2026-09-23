from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import asyncio


def cpu_cb(task: asyncio.Task | asyncio.Future):
    result = task.exception() or task.result()
    print(f'Расчетная задача завершена с результатом {result!r}')


def io_cb(task: asyncio.Task | asyncio.Future):
    result = task.exception() or task.result()
    print(f'Блокирующая задача завершена с результатом {result!r}')


def async_cb(task: asyncio.Task | asyncio.Future):
    result = task.exception() or task.result()
    print(f'Корутина завершена с результатом {result!r}')


def has_cpu_true(fn):
    return getattr(fn, 'cpu', None)


async def main():
    coros = []
    cpu_funcs = []
    io_funcs = []
    [
        coros.append(entity) if asyncio.iscoroutine(entity)
        else cpu_funcs.append(entity) if has_cpu_true(entity)
        else io_funcs.append(entity)
        for entity in entities
    ]

    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=len(io_funcs)) as th_pool, ProcessPoolExecutor() as pr_pool:
        cpu_tasks = [loop.run_in_executor(pr_pool, fn) for fn in cpu_funcs]
        for cpu_task in cpu_tasks:
            cpu_task.add_done_callback(cpu_cb)
        io_tasks = [loop.run_in_executor(th_pool, fn) for fn in io_funcs]
        for io_task in io_tasks:
            io_task.add_done_callback(io_cb)
        coro_tasks = [asyncio.create_task(coro) for coro in coros]
        for coro_task in coro_tasks:
            coro_task.add_done_callback(async_cb)
        await asyncio.gather(*cpu_tasks, *io_tasks, *coro_tasks, return_exceptions=True)


if __name__ == '__main__':
    asyncio.run(main())

entities = []


# alt


def cb(task: asyncio.Task | asyncio.Future):
    if exc := task.exception():
        result = repr(exc)
    else:
        result = task.result()
    print(f"{task.type_name} завершена с результатом {result}")


async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as th_pool, ProcessPoolExecutor() as pr_pool:
        io_futures = []
        cpu_futures = []
        async_coro = []
        for elem in entities:
            if asyncio.iscoroutine(elem):
                f = asyncio.create_task(elem)
                f.type_name = "Корутина"
                async_coro.append(f)
                f.add_done_callback(cb)
            elif hasattr(elem, "cpu"):
                f = loop.run_in_executor(pr_pool, elem)
                f.type_name = "Расчетная задача"
                cpu_futures.append(f)
                f.add_done_callback(cb)
            else:
                f = loop.run_in_executor(th_pool, elem)
                f.type_name = "Блокирующая задача"
                io_futures.append(f)
                f.add_done_callback(cb)
        await asyncio.gather(*io_futures, *cpu_futures, *async_coro, return_exceptions=True)
