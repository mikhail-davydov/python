import asyncio
from typing import Protocol


class LLMEngine(Protocol):
    async def generate(self, prompt: str, max_tokens: int) -> str:
        ...


async def deep_healthcheck(engine: LLMEngine, timeout: float = 5.0) -> bool:
    """
Проверяет, может ли модель выполнить inference за заданное время.
    """
    try:
        await asyncio.wait_for(
            engine.generate("Ping", max_tokens=5),
            timeout=timeout
        )
        return True
    except (asyncio.TimeoutError, Exception):
        return False