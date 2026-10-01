from asyncio import Semaphore, Task

import asyncio
import functools
import math
import psutil

INIT_LIMIT = 3
LOAD_RATE_LIMIT_PERCENT = 4
INTERVAL_SECONDS = 1
CORO_COUNT = 20
HEAVY_LOAD_OPS = 10_000_000


class DynamicSemaphore(Semaphore):
    def __init__(self, limit=1):
        super().__init__(limit)
        self.max = self._value
        self.min = self._value

    async def check_load(self):
        print(f'Initial state: {self}')
        while True:
            cpu_load_rate = psutil.cpu_percent(interval=1)
            memory_load_rate = psutil.virtual_memory().percent
            print(f'{cpu_load_rate=}, {memory_load_rate=}')

            # if cpu_load_rate > LOAD_RATE_LIMIT_PERCENT or memory_load_rate > LOAD_RATE_LIMIT_PERCENT:
            if cpu_load_rate > LOAD_RATE_LIMIT_PERCENT:
                self._value -= 1
                if self._value < self.min:
                    self.min = self._value
            else:
                self._value += 1
                if self._value > self.max:
                    self.max = self._value
            print(self)

            await asyncio.sleep(INTERVAL_SECONDS)


def stop_monitoring(sema: DynamicSemaphore, task: Task):
    print(f'{sema.min=}, {sema.max=}')
    print('Stop monitoring')


async def start_hub():
    sema = DynamicSemaphore(INIT_LIMIT)
    tasks = [asyncio.create_task(worker(sema)) for _ in range(CORO_COUNT)]
    monitoring_task = asyncio.create_task(sema.check_load())
    monitoring_task.add_done_callback(functools.partial(stop_monitoring, sema))
    await asyncio.gather(*tasks)
    monitoring_task.cancel()


async def worker(sema: Semaphore):
    async with sema:
        await coro()


async def coro():
    await asyncio.sleep(1)
    heavy_cpu_task()
    # task_name = asyncio.current_task().get_name()
    # print(f'{task_name} did some work')


def heavy_cpu_task():
    total = 0.0
    for i in range(1, HEAVY_LOAD_OPS):
        val = math.log(i) + math.sin(i) * math.cos(i)
        total += val
    return total


async def main():
    await asyncio.create_task(start_hub())


if __name__ == '__main__':
    asyncio.run(main())
