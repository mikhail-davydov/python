import socket
from typing import Tuple


# допишите функцию сервера
def server(address: Tuple[str, int]) -> None:
    with socket.socket() as server_socket:
        server_socket.bind(address)
        server_socket.listen(1)
        conn, addr = server_socket.accept()
        data: str = conn.recv(1024).decode()
        # total = sum(int(num) for num in data.split())
        total = sum(map(int, data.split()))
        print(total)


if __name__ == '__main__':
    server(('localhost', 5555))
