from concurrent.futures import ThreadPoolExecutor

import asyncio
import threading
import time


async def coro(i: int):
    await asyncio.sleep(i / 10)
    task = asyncio.current_task()
    print(f"Задача {task.get_name()} выполнилась")


def blocking(i: int):
    time.sleep(i / 10)  # <-! блокирующее ожидание
    thread = threading.current_thread()
    print(f"blocking выполнилась потоком {thread.name}\n", end="")


# async def main():
#     loop = asyncio.get_running_loop()
#     with ThreadPoolExecutor(16, thread_name_prefix="Поток пула №") as executor:
#         await asyncio.gather(
#             *(loop.run_in_executor(executor, blocking, i) for i in range(1, 17)),
#             *(coro(i) for i in range(1, 17)),
#         )

async def run_in_pool(executor, func, *args):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, func, *args)


# async def main():
#     tasks = []
#     with ThreadPoolExecutor(16, thread_name_prefix="Поток пула №") as executor:
#         for i in range(1, 17):
#             tasks.append(asyncio.create_task(coro(i)))
#         for i in range(1, 17):
#             tasks.append(asyncio.create_task(run_in_pool(executor, blocking, i)))
#         for task in tasks:
#             await task


async def main():
    with ThreadPoolExecutor(16, thread_name_prefix="Поток пула №") as executor:
        async with asyncio.TaskGroup() as tg:
            for i in range(1, 17):
                tg.create_task(coro(i))
                tg.create_task(run_in_pool(executor, blocking, i))


if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(main())
    print(f"\nAll done in {time.perf_counter() - start_time:.2f}")
