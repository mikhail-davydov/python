from concurrent.futures import ThreadPoolExecutor

import asyncio


async def main():
    coros = []
    funcs = []
    for entity in entities:
        if asyncio.iscoroutine(entity):
            coros.append(entity)
        else:
            funcs.append(entity)

    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(len(funcs)) as executor:
        func_tasks = [loop.run_in_executor(executor, func) for func in funcs]
        await asyncio.gather(*func_tasks, *coros)


if __name__ == '__main__':
    asyncio.run(main())

entities = []
