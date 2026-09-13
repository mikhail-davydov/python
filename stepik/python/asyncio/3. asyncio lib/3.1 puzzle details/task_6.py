import asyncio


async def my_coroutine_1() -> str:
    return 'first'


async def my_coroutine_2() -> str:
    return 'second'


async def my_coroutine_3() -> str:
    return 'third'


async def main():
    coros = (my_coroutine_1(), my_coroutine_2(), my_coroutine_3())
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(coro) for coro in coros]
    return [task.result() for task in tasks]


if __name__ == '__main__':
    res = asyncio.run(main())
    print(*res, sep='\n')
