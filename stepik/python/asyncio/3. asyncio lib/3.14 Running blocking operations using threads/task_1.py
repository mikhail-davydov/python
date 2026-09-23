import asyncio


async def main():
    tasks = []
    for entity in entities:
        if asyncio.iscoroutine(entity):
            tasks.append(asyncio.create_task(entity))
        else:
            tasks.append(asyncio.create_task(asyncio.to_thread(entity)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())

entities = []
