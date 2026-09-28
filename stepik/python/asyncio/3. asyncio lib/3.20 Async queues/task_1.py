import asyncio

AsyncQueueType = asyncio.Queue | asyncio.LifoQueue | asyncio.PriorityQueue

TIMEOUT = 0.2


async def consumer(queue: AsyncQueueType):
    current = asyncio.current_task().get_name()
    while True:
        task = asyncio.create_task(queue.get())
        done, _ = await asyncio.wait([task], timeout=TIMEOUT)
        if task in done:
            print(f'{current} извлек элемент очереди {task.result()!r}')
        else:
            break
    print(f'Работа {current} завершена!')


# alt

async def consumer(queue: AsyncQueueType):
    task_name = asyncio.current_task().get_name()
    while True:
        try:
            elem = await asyncio.wait_for(queue.get(), timeout=0.2)
            print(f"{task_name} извлек элемент очереди {elem!r}")
        except asyncio.TimeoutError:
            print(f"Работа {task_name} завершена!")
            break


# alt

async def consumer(queue: AsyncQueueType):
    cur_task_name = asyncio.current_task().get_name()
    while True:
        try:
            async with asyncio.timeout(0.2):
                elem = await queue.get()
                print(f"{cur_task_name} извлек элемент очереди {repr(elem)}")
        except asyncio.TimeoutError:
            print(f"Работа {cur_task_name} завершена!")
            break
