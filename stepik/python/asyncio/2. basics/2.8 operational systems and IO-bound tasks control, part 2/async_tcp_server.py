import selectors
import socket
import time
from typing import Tuple


def create_server(address: Tuple[str, int]) -> socket.socket:
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(address)
    server_socket.listen()
    return server_socket


def handler(data: bytes) -> bytes:
    try:
        print(f"received data {data}")
        time.sleep(1)
        numbers = [int(n) for n in data.decode().split()]
        res = sum(numbers)
    except Exception as er:
        msg = repr(er)
    else:
        msg = f'{"+".join(map(str, numbers))}={res}'
    finally:
        return msg.encode()


def accept_conn(server_sock: socket.socket, selector: selectors.BaseSelector) -> None:
    try:
        conn, addr = server_sock.accept()
        print(f"Connection from {addr}")
        selector.register(conn, selectors.EVENT_READ)
    except socket.error as error:
        print(f"Error accepting connection: {error}")


def send_response(client_sock: socket.socket) -> None:
    data = client_sock.recv(1024)
    response = handler(data)
    client_sock.send(response)


def event_loop(server_socket: socket.socket) -> None:
    with selectors.DefaultSelector() as selector:
        selector.register(server_socket, selectors.EVENT_READ)
        while True:
            sockets = selector.select(2)

            if not sockets:
                print('no connection right now')

            for k, _ in sockets:
                sock: socket.socket = k.fileobj
                if sock is server_socket:
                    accept_conn(sock, selector)
                else:
                    try:
                        send_response(sock)
                    except socket.error as error:
                        print(f"Error receiving data: {error}")
                        sock.close()
                        selector.unregister(sock)


if __name__ == "__main__":
    address = ("localhost", 5555)
    server_socket = create_server(address)
    event_loop(server_socket)
