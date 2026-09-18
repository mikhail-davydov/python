import asyncio


async def main():
    tasks = [asyncio.create_task(coro) for coro in coroutines]
    await asyncio.wait(tasks)
    [print(task.result()) for task in tasks]


if __name__ == '__main__':
    asyncio.run(main())

coroutines = []
