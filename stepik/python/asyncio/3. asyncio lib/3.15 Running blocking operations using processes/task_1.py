from concurrent.futures import ProcessPoolExecutor

import asyncio


async def main():
    coros = []
    funcs = []
    [
        coros.append(entity)
        if asyncio.iscoroutine(entity) else funcs.append(entity)
        for entity in entities
    ]

    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        func_tasks = [loop.run_in_executor(executor, func) for func in funcs]
        await asyncio.gather(*func_tasks, *coros)


if __name__ == '__main__':
    asyncio.run(main())

entities = []
