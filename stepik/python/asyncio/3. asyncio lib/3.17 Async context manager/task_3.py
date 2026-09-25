import contextlib
import asyncio


@contextlib.asynccontextmanager
async def conn_ssh():
    conn = AsyncThrSSH()
    try:
        yield conn
    finally:
        await conn.close()


class AsyncThrSSH:
    async def connect(self):
        pass

    async def close(self):
        pass
