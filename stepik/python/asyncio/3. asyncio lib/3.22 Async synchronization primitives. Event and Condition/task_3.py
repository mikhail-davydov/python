import asyncio


class TimeoutCondition(asyncio.Condition):
    async def wait_for(self, predicate, timeout: int | float = None):
        try:
            return await asyncio.wait_for(super().wait_for(predicate), timeout=timeout)
        except TimeoutError:
            return predicate()


# alt
class TimeoutCondition(asyncio.Condition):
    async def wait_for(self, predicate, timeout: int | float | None = None):
        try:
            async with asyncio.timeout(timeout):
                return await super().wait_for(predicate)
        except asyncio.TimeoutError:
            return predicate()
