import asyncio


async def coroutine_number():
    print("1")
    await asyncio.sleep(0)
    print("2")


async def coroutine_symbol():
    print("A")
    await asyncio.sleep(0)
    print("B")


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(coroutine_number())
        tg.create_task(coroutine_symbol())


if __name__ == '__main__':
    asyncio.run(main())
