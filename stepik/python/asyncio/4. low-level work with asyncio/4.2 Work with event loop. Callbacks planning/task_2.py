from asyncio import Barrier

import asyncio
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
