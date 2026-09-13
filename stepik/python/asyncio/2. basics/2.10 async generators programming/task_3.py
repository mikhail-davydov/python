import socket
from collections import deque
from typing import TypeAlias, Iterable

import select

Task: TypeAlias = Iterable[tuple[str, socket.socket]]


def server(tasks: deque[Task]) -> Task:
    server_sock = socket.socket()
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(address)
    server_sock.listen()
    while True:
        yield 'accept', server_sock
        conn, addr = server_sock.accept()
        tasks.append(client(conn))


def client(conn: socket.socket):
    while True:
        yield 'recv', conn
        data = conn.recv(1024)
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


def event_loop() -> None:
    tasks = deque()
    tasks.append(server(tasks))

    read_tasks = {}
    write_tasks = {}

    total_idle = 0
    while True:
        if not tasks:
            # ready_to_read, ready_to_write, _ = select.select(read_tasks, write_tasks, [])
            ready_to_read, ready_to_write, _ = select.select(read_tasks, write_tasks, [], 1)

            if not ready_to_read and not ready_to_write:
                total_idle += 1
                idle_handler()

            if total_idle > 1:
                return

            for conn in ready_to_read:
                tasks.append(read_tasks.pop(conn))
            for conn in ready_to_write:
                tasks.append(write_tasks.pop(conn))

        if not tasks:
            continue

        try:
            total_idle = 0
            task = tasks.popleft()
            action, conn = next(task)
            match action:
                case 'send':
                    write_tasks[conn] = task
                case _:
                    read_tasks[conn] = task
        except socket.error:
            print('Потеря связи с клиентом')
            conn.close()


def idle_handler():
    print('idle handler')


if __name__ == '__main__':
    address = ('localhost', 5555)
    event_loop()
