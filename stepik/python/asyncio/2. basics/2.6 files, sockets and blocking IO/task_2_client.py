import socket

from typing import Tuple


# допишите функцию клиента
def client(address: Tuple[str, int], msg: str) -> None:
    client_sock = socket.socket()
    address = address
    client_sock.connect(address)
    client_sock.send(msg.encode())

    client_sock.close()


if __name__ == '__main__':
    client(('localhost', 5555), '11 345 23 11902 23')

# alt

import socket
from typing import Tuple


# допишите функцию клиента
def client(address: Tuple[str, int], msg: str) -> None:
    with socket.socket() as client_sock:
        client_sock.connect(address)
        client_sock.send(msg.encode())
