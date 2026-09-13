import asyncio


async def main():
    tasks = [asyncio.create_task(coro) for coro in (my_coroutine_1(), my_coroutine_2(), my_coroutine_3())]
    return [await task for task in tasks]


if __name__ == '__main__':
    res = asyncio.run(main())
    print(*res, sep='\n')


async def my_coroutine_1() -> str:
    return 'first'


async def my_coroutine_2() -> str:
    return 'second'


async def my_coroutine_3() -> str:
    return 'third'
