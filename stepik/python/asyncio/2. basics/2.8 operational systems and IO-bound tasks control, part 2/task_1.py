import selectors

import socket
from typing import Callable, List


def idle_selectors(sockets: List[socket.socket], idle_handler: Callable, timeout: int | float) -> List[socket.socket]:
    with selectors.DefaultSelector() as sel:
        for sock in sockets:
            sel.register(sock, selectors.EVENT_READ)

        socks = sel.select(timeout)
        if not socks:
            idle_handler()
        return [sock.fileobj for sock, _ in socks]


# alt

import socket
import selectors
from typing import Callable, List, Tuple


def idle_selectors(sockets: List[socket.socket], idle_handler: Callable, timeout: int | float) -> List[socket.socket]:
    with selectors.DefaultSelector() as sel:
        [sel.register(sock, selectors.EVENT_READ) for sock in sockets]
        if not (sock_to_read := sel.select(timeout)):
            idle_handler()
        return [k.fileobj for k, _ in sock_to_read]
