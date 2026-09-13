from concurrent.futures import ThreadPoolExecutor

import socket
from typing import Any


def server() -> None:
    server_sock = socket.socket()
    address = ("localhost", 5555)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(address)
    server_sock.listen()
    print(f"Server listening on {address}")

    with ThreadPoolExecutor(max_workers=10) as executor:
        try:
            while True:
                conn, addr = server_sock.accept()
                executor.submit(handle_client, conn, addr)
        except KeyboardInterrupt:
            print("\nServer shutting down...")
        finally:
            server_sock.close()


def handle_client(conn: socket, addr: Any):
    while data := conn.recv(1024):  # получаем и обрабатываем запросы
        print(f"received data {data} from {addr}")
        msg = data.decode()

        try:
            numbers = [int(n) for n in msg.split()]
            res = sum(numbers)
        except Exception as er:
            msg = repr(er)
        else:
            msg = f'{"+".join(map(str, numbers))}={res}'
        finally:
            conn.send(msg.encode())


if __name__ == '__main__':
    server()
