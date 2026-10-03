from asyncio import Barrier

import asyncio
import random
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


async def coro(barrier: SimpleBarrier):
    task_name = asyncio.current_task().get_name()
    await asyncio.sleep(random.random())
    print(f"{task_name} достиг барьера №1")
    try:
        await barrier.wait()
    except TimeoutError:
        print(f"{task_name} преодолел барьер №1 по таймауту!!!")
    else:
        print(f"{task_name} успешно преодолел барьер №1")
    await asyncio.sleep(random.random())
    print(f"\t{task_name} достиг барьера №2")
    try:
        await barrier.wait()
    except TimeoutError:
        print(f"\t{task_name} преодолел барьер №2 по таймауту!!!")
    else:
        print(f"\t{task_name} успешно преодолел барьер №2")


async def main():
    print("Тест №1. Выполнение без преодоления барьера по таймауту.")
    barrier = SimpleBarrier(parties=3, action=finalizer, timeout=2)
    tasks = [asyncio.create_task(coro(barrier), name=f"Task#{i}") for i in range(1, 4)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
