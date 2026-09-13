import asyncio


async def main():
    res_1 = await my_coroutine_1()
    res_2 = await my_coroutine_2()
    res_3 = await my_coroutine_3()
    return res_1, res_2, res_3


if __name__ == '__main__':
    res = asyncio.run(main())
    print(*res, sep='\n')


async def my_coroutine_1() -> str:
    return 'first'


async def my_coroutine_2() -> str:
    return 'second'


async def my_coroutine_3() -> str:
    return 'third'


# alt

import asyncio

async def main():
    results = [await coro for coro in (my_coroutine_1(), my_coroutine_2(), my_coroutine_3())]
    print(*results, sep="\n")

if __name__ == '__main__':
    asyncio.run(main())