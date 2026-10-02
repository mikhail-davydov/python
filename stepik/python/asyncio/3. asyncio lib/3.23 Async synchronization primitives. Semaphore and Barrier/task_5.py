from asyncio import Barrier

import asyncio
import random

N = 4
barrier = Barrier(N)


# Разделите барьером логику работы корутины на три этапа
async def coro():
    await stage1()
    if await barrier.wait() == barrier.parties - 1:
        final1()
    await stage2()
    if await barrier.wait() == barrier.parties - 1:
        final2()
    await stage3()


# alt
# async def coro():
#     await stage1()
#     n = await barrier.wait()
#     if n == barrier.parties-1:
#         final1()
#     await stage2()
#     n = await barrier.wait()
#     if n == barrier.parties-1:
#         final2()
#     await stage3()


def final2():
    name = asyncio.current_task().get_name()
    print(f'{name} вызвала final2')


def final1():
    name = asyncio.current_task().get_name()
    print(f'{name} вызвала final1')


async def stage3():
    await asyncio.sleep(random.randint(1, 3))
    name = asyncio.current_task().get_name()
    print(f'{name} выполнила stage3')


async def stage2():
    await asyncio.sleep(random.randint(1, 3))
    name = asyncio.current_task().get_name()
    print(f'{name} выполнила stage2')


async def stage1():
    await asyncio.sleep(random.randint(1, 3))
    name = asyncio.current_task().get_name()
    print(f'{name} выполнила stage1')


async def main():
    coros = [asyncio.create_task(coro()) for _ in range(N)]
    await asyncio.gather(*coros)


if __name__ == '__main__':
    asyncio.run(main())
