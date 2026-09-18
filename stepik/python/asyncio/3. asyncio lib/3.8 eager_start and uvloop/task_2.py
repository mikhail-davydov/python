import asyncio
import random
import time
import uvloop

cashed_data = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}


async def get_request(n: int):
    await asyncio.sleep(0, n)


async def get_data(n: int):
    if n in cashed_data:
        return cashed_data[n]
    return await get_request(n)


async def main():
    async with asyncio.TaskGroup() as tg:
        for _ in range(50_000):
            i = random.randint(1, 10)
            tg.create_task(get_data(i))


start_time = time.perf_counter()

if __name__ == '__main__':
    uvloop.run(main())

# alt

if __name__ == '__main__':
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.set_task_factory(asyncio.eager_task_factory)
    loop.run_until_complete(main())

# alt

if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.new_event_loop()
    loop.set_task_factory(asyncio.eager_task_factory)
    loop.run_until_complete(main())

# alt

if __name__ == '__main__':
    with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
        runner.get_loop().set_task_factory(asyncio.eager_task_factory)
        runner.run(main())
