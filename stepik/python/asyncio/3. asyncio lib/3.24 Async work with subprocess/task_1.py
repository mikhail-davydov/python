import asyncio
import sys


async def sub_proc(code: str) -> str:
    process = await asyncio.create_subprocess_exec(
        sys.executable,
        '-c',
        code,
        stdout=asyncio.subprocess.PIPE,
    )
    stdout, _ = await process.communicate()
    return stdout.decode().rstrip()


# alt
async def sub_proc(code: str) -> str:
    process = await asyncio.create_subprocess_exec(
        sys.executable,
        '-c',
        code,
        stdout=asyncio.subprocess.PIPE,
    )

    result = await process.stdout.read()
    return result.decode()
