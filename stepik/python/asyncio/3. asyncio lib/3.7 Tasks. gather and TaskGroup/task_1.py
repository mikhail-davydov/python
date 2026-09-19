import asyncio

results = []


async def main():
    results.extend(await asyncio.gather(*coroutines, return_exceptions=True))


if __name__ == '__main__':
    asyncio.run(main())

coroutines = []

# alt

async def main():
    return await asyncio.gather(*coroutines, return_exceptions=True)

if __name__ == '__main__':
    results = asyncio.run(main())