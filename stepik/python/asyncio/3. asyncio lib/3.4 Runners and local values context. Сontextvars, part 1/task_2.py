import asyncio
import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format=logging.BASIC_FORMAT,
)


async def my_coroutine():
    print("start", end=" ")
    await asyncio.sleep(1)
    print("and finish")
    return "i'm ok"


async def main():
    return await my_coroutine()


if __name__ == '__main__':
    with asyncio.Runner() as runner:
        print(runner.run(main()))
