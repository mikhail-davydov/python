import asyncio


# original task: signal element
async def producer(queue: asyncio.Queue):
    async for elem in json_gen():
        await queue.put(elem)
    await queue.put(None)


async def consumer(queue: asyncio.Queue):
    while True:
        elem = await queue.get()
        if elem is None:
            await queue.put(None)
            final()
            break
        await registrator(elem)


async def producer_consumer(queue: asyncio.Queue):
    await asyncio.gather(producer(queue), consumer(queue), consumer(queue))


# solution: no signal element

async def producer(queue: asyncio.Queue):
    async for elem in json_gen():
        await queue.put(elem)


async def consumer(queue: asyncio.Queue):
    while True:
        elem = await queue.get()
        await registrator(elem)
        queue.task_done()


async def producer_consumer(queue: asyncio.Queue):
    producer_task = asyncio.create_task(producer(queue))
    asyncio.create_task(consumer(queue))
    asyncio.create_task(consumer(queue))

    await producer_task
    await queue.join()
    final()


# alt

async def all_done(queue: asyncio.Queue, consumers: list[asyncio.Task]):
    await producer(queue)
    await queue.join()
    final()
    for consumer in consumers:
        consumer.cancel()


async def producer_consumer(queue: asyncio.Queue):
    consumers = [asyncio.create_task(consumer(queue)) for _ in range(2)]
    await asyncio.gather(*consumers, all_done(queue, consumers), return_exceptions=True)


# templates

async def json_gen():
    yield


async def registrator(item):
    pass


def final():
    pass
