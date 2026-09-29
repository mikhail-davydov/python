from asyncio import Lock

import asyncio
import time

N = 5
lock = Lock()


async def part_1():
    await asyncio.sleep(1)


async def part_2():
    await asyncio.sleep(2)


async def part_3():
    await asyncio.sleep(3)


async def coro():
    await part_1()
    async with lock:
        await part_2()
        await part_3()


async def main():
    start = time.perf_counter()
    tasks = [asyncio.create_task(coro()) for i in range(N)]
    await asyncio.gather(*tasks)
    print(f'Done in {time.perf_counter() - start:.2f}')


if __name__ == '__main__':
    asyncio.run(main())
