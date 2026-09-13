import socket
from collections import deque
from collections.abc import Iterable
from typing import TypeAlias

import select

Task: TypeAlias = Iterable[tuple[str, socket.socket]]


def server() -> Task:
    server_sock = socket.socket()
    address = ("localhost", 5555)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(address)
    server_sock.listen()
    while True:
        yield 'accept', server_sock
        conn, addr = server_sock.accept()
        print(f"Connection from {addr}")
        tasks.append(client(conn))


def client(conn: socket.socket) -> Task:
    while True:
        yield 'recv', conn
        data = conn.recv(1024)
        print(f"received data {data}")
        try:
            numbers = [int(n) for n in data.decode().split()]
            res = sum(numbers)
        except Exception as er:
            msg = repr(er)
        else:
            msg = f'{"+".join(map(str, numbers))}={res}'
        finally:
            yield 'send', conn
            conn.send(msg.encode())


def event_loop():
    wait_for_read = {}
    wait_for_write = {}

    while True:
        if not tasks:
            ready_to_read, ready_to_write, _ = select.select(wait_for_read, wait_for_write, [], 5)

            if not ready_to_read and not ready_to_write:
                print('No connection to server during 5 secs. Stop server.')
                return

            for conn in ready_to_read:
                tasks.append(wait_for_read.pop(conn))
            for conn in ready_to_write:
                tasks.append(wait_for_write.pop(conn))

        try:
            task = tasks.popleft()
            method, conn = next(task)
            if method == 'send':
                wait_for_write[conn] = task
            else:
                wait_for_read[conn] = task
        except socket.error:
            print('Socket error')


if __name__ == "__main__":
    tasks = deque()
    tasks.append(server())
    event_loop()
