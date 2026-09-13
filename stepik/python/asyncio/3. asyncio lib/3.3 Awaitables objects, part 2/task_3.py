import asyncio


async def my_coroutine_1(): ...
async def my_coroutine_2(): ...
async def my_coroutine_3(): ...
async def my_coroutine_4(): ...
async def my_coroutine_5(): ...
async def my_coroutine_6(): ...


async def main():
    coros = [
        my_coroutine_1(),
        my_coroutine_2(),
        my_coroutine_3(),
        my_coroutine_4(),
        my_coroutine_5(),
        my_coroutine_6(),
    ]
    await asyncio.gather(*coros)


if __name__ == '__main__':
    asyncio.run(main())


# alt

async def main():
    coros = [my_coroutine_1, my_coroutine_2, my_coroutine_3, my_coroutine_4, my_coroutine_5, my_coroutine_6]
    async with asyncio.TaskGroup() as tg:
        for coro in coros:
            tg.create_task(coro())

if __name__ == '__main__':
    asyncio.run(main())




