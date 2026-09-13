import select

import socket
from typing import Callable, List


def idle_select(sockets: List[socket.socket], idle_handler: Callable, timeout: int | float) -> List[socket.socket]:
    ready_to_read, _, _ = select.select(sockets, [], [], timeout)
    if not ready_to_read:
        idle_handler()
    return ready_to_read
