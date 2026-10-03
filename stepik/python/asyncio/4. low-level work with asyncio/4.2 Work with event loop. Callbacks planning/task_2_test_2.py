from asyncio import Barrier

import asyncio
import time
from typing import Callable, Optional


class SimpleBarrier(Barrier):
    def __init__(
            self,
            parties: int,
            action: Optional[Callable[[], None]] = None,
            timeout: Optional[float] = None,
    ):
        super().__init__(parties)
        self._action = action
        self._delay = timeout

    async def wait(self):
        task = asyncio.ensure_future(super().wait())
        done, pending = await asyncio.wait([task], timeout=self._delay)

        if done:
            result = done.pop().result()
            if result == self.parties - 1 and self._action:
                self._action()
            return result

        raise TimeoutError


def finalizer():
    task_name = asyncio.current_task().get_name()
    print(f"-> Этап завершен! {task_name} вызывает указанный action")


async def coro_time(barrier: SimpleBarrier):
    task_name = asyncio.current_task().get_name()
    if task_name == "Task#2":
        timer = 1.1
    else:
        timer = 0
    await asyncio.sleep(timer)
    print(f"{task_name} достиг барьера №1")
    try:
        start_time = time.perf_counter()
        await barrier.wait()
    except TimeoutError:
        print(f"{task_name} преодолел барьер по таймауту!!!, ждал {time.perf_counter() - start_time:.1f}с.")
    else:
        print(f"{task_name} успешно преодолел барьер")


async def main():
    print("\nТест №2. Выполнение с преодолением барьера по таймауту timeout=1")
    barrier = SimpleBarrier(parties=3, action=finalizer, timeout=1)
    tasks = [asyncio.create_task(coro_time(barrier), name=f"Task#{i}") for i in range(1, 4)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
