import asyncio

def get_loop() -> tuple[bool, asyncio.BaseEventLoop]:
    try:
        return True, asyncio.get_running_loop()
    except RuntimeError:
        return False, asyncio.new_event_loop()
