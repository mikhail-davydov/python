import asyncio
import time

TIMES = 1000


async def coro():
    await asyncio.sleep(0)


def func():
    time.sleep(0)


async def main():
    start_time = time.perf_counter()
    tasks_coro = [asyncio.create_task(coro()) for _ in range(TIMES)]
    await asyncio.wait(tasks_coro)
    print(f"test#1 coro, all done in {time.perf_counter() - start_time:.2f}")

    start_time = time.perf_counter()
    tasks_func = [asyncio.create_task(asyncio.to_thread(func)) for _ in range(TIMES)]
    await asyncio.wait(tasks_func)
    print(f"test#2 threads, all done in {time.perf_counter() - start_time:.2f}")


if __name__ == '__main__':
    asyncio.run(main())


# alt

async def main():
    start_time = time.perf_counter()
    await asyncio.gather(*(coro() for _ in range(TIMES)))
    print(f"test#1 coro, all done in {time.perf_counter() - start_time:.2f}")

    start_time = time.perf_counter()
    await asyncio.gather(*(asyncio.to_thread(func) for _ in range(TIMES)))
    print(f"test#2 threads, all done in {time.perf_counter() - start_time:.2f}")
