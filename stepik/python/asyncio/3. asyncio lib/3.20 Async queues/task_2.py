import asyncio
from random import uniform

AsyncQueueType = asyncio.Queue | asyncio.LifoQueue | asyncio.PriorityQueue

TIMEOUT = 0.4


async def timeout_coro():
    await asyncio.sleep(TIMEOUT)
    print('Очередь переполнена, требуется больше потребителей!')


async def producer(queue: AsyncQueueType):
    task_name = asyncio.current_task().get_name()
    async for item in json_gen():
        timeout_task = asyncio.create_task(timeout_coro())
        await queue.put(item)
        timeout_task.cancel()
        print(f'{task_name} поместил {item!r} в очередь')


# test

async def json_gen():
    for item in range(10):
        yield item
    yield None


async def consumer(queue: AsyncQueueType):
    while True:
        await asyncio.sleep(uniform(0, 1))
        i = await queue.get()
        print(f"consumer извлек из очереди {i}")
        if i is None:
            print("consumer завершил работу")
            break


async def main():
    my_queue = asyncio.Queue(5)
    await asyncio.gather(producer(my_queue), consumer(my_queue))


if __name__ == '__main__':
    asyncio.run(main())


# alt

async def producer(queue: AsyncQueueType):
    task_name = asyncio.current_task().get_name()
    async for elem in json_gen():
        try:
            task = asyncio.create_task(queue.put(elem))
            task.add_done_callback(lambda _: print(f"{task_name} поместил {elem!r} в очередь"))
            await asyncio.wait_for(asyncio.shield(task), 0.4)
        except asyncio.TimeoutError:
            print("Очередь переполнена, требуется больше потребителей!")

# alt

async def producer(queue: AsyncQueueType):
    current_task_name = asyncio.current_task().get_name()
    async for elem in json_gen():
        try:
            task = asyncio.create_task(queue.put(elem))
            await asyncio.wait_for(asyncio.shield(task), timeout=0.4)
        except asyncio.TimeoutError:
            print('Очередь переполнена, требуется больше потребителей!')
            await task # дожидаемся
        finally:
            print(f'{current_task_name} поместил {repr(elem)} в очередь')