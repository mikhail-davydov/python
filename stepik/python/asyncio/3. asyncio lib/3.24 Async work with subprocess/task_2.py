import asyncio
import sys


async def sub_proc(code: str, timeout: int | float) -> str:
    process = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE,
        # stderr=asyncio.subprocess.PIPE,
    )
    try:
        stdout, _ = await asyncio.wait_for(process.communicate(), timeout=timeout)
        # stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout)
        if process.returncode != 0:
            return 'Exception'
        return stdout.decode().strip()
    except TimeoutError:
        process.terminate()
        await process.communicate()
        return 'TimeoutError'


# alt
async def sub_proc(code: str, timeout: int | float) -> str:
    subprocess = await asyncio.create_subprocess_exec(sys.executable, "-c", code,
                                                      stdout=asyncio.subprocess.PIPE,
                                                      stderr=asyncio.subprocess.PIPE,
                                                      )
    try:
        output_data, output_exc = await asyncio.wait_for(subprocess.communicate(), timeout=timeout)
    except TimeoutError:
        subprocess.terminate()
        await subprocess.wait()
        return "TimeoutError"
    if output_exc:
        return "Exception"
    return output_data.decode().rstrip()
