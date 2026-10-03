import asyncio
from typing import Any, Optional, Union


async def simple_sleep(delay: Union[int, float] = 0, result: Optional[Any] = None) -> Optional[Any]:
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    loop.call_later(delay, fut.set_result, result)
    return await fut
