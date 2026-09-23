from concurrent.futures import ThreadPoolExecutor

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
    with ThreadPoolExecutor(len(funcs)) as executor:
        func_tasks = [loop.run_in_executor(executor, func) for func in funcs]
        results = [await task for task in asyncio.as_completed(func_tasks + coros)]
        print(results)


if __name__ == '__main__':
    asyncio.run(main())

entities = []
