import asyncio
import contextvars


async def print_msg():
    msg = ctx.get(ctx_msg, 'failure')
    fileno = ctx.get(ctx_fileno, 'failure')
    permission = ctx.get(ctx_permission, 'guest')
    print(f'{msg}, fileno={fileno}, {permission}')


if __name__ == '__main__':
    ctx_msg = contextvars.ContextVar('ctx_msg')
    ctx_fileno = contextvars.ContextVar('ctx_fileno')
    ctx_permission = contextvars.ContextVar('ctx_permission')
    ctx = contextvars.copy_context()
    with asyncio.Runner() as runner:
        runner.run(print_msg())
