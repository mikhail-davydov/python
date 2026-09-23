from concurrent.futures import ThreadPoolExecutor  # импортируем пул потоков

import asyncio
import threading
import time


def blocking():
    time.sleep(1)
    print(f"blocking успешно выполнилась потоком {threading.current_thread().name}\n", end="")


# async def main():
#     loop = asyncio.get_running_loop()
#     # создаем пул с 16 потоками и назначаем префикс
#     executor = ThreadPoolExecutor(16, thread_name_prefix="pool_worker_№")
#     loop.set_default_executor(executor)
#     await asyncio.gather(*(asyncio.to_thread(blocking) for _ in range(16)))  # 16 задач!


async def main():
    loop = asyncio.get_running_loop()
    executor = ThreadPoolExecutor(16, thread_name_prefix="pool_worker_№")
    await asyncio.gather(*(loop.run_in_executor(executor, blocking) for _ in range(16)))


if __name__ == '__main__':

    start_time = time.perf_counter()
    asyncio.run(main())
    print(f"\nAll done in {time.perf_counter() - start_time:.2f}")
