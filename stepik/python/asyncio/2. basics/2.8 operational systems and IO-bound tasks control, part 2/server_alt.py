import selectors
import socket
import sys
import threading
from time import sleep, perf_counter
from typing import Tuple

CLIENTS, REQUESTS, SERVER_DELAY = (5000, 100, 0) if False else (3, 3, 1)


def create_server(address: Tuple[str, int]) -> socket.socket:
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(address)
    server_socket.listen()
    return server_socket  # возвращаем настроенный серверный сокет


def handler(data: bytes) -> bytes:
    try:
        print(f"received data {data}")
        numbers = [int(n) for n in data.decode().split()]
        res = sum(numbers)
    except Exception as er:
        msg = repr(er)
    else:
        msg = f'{"+".join(map(str, numbers))}={res}'
    finally:
        return msg.encode()


class ServerSelector(selectors.DefaultSelector):
    def __init__(self, server_socket: socket.socket):
        super().__init__()
        self.total_clients = -1
        self.max_clients = -1
        self.clients_count = -1
        self.register(server_socket, selectors.EVENT_READ)

    def register(self, fileobj, events, data=None):
        result = super().register(fileobj, events, data)
        self.clients_count += 1
        self.total_clients += 1
        self.max_clients = max(self.max_clients, self.clients_count)
        return result

    def unregister(self, fileobj):
        result = super().unregister(fileobj)
        self.clients_count -= 1
        return result

    def shutdown(self):
        for fd in tuple(self.get_map()):
            self.unregister(fd).fileobj.close()

    def is_full(self):
        return sys.platform == 'win32' and self.clients_count >= 511


def accept_conn(server_sock: socket.socket, selector: ServerSelector) -> None:
    if selector.is_full():
        return
    try:
        conn, addr = server_sock.accept()
        print(f"Connection from {addr}, total active: {selector.clients_count}")
        selector.register(conn, selectors.EVENT_READ)
    except socket.error as exc:
        print(f"Error accepting connection: {exc}")


def send_response(client_sock: socket.socket) -> None:
    if data := client_sock.recv(1024):
        sleep(SERVER_DELAY)
        response = handler(data)
        client_sock.send(response)
    else:
        raise socket.error('client disconnected')


def close(selector: ServerSelector):
    input()
    selector.shutdown()


def event_loop(server_socket: socket.socket) -> None:
    with ServerSelector(server_socket) as selector:
        threading.Thread(target=close, args=(selector,), name='CloseHandler', daemon=True).start()
        while selector.clients_count >= 0:
            ready = selector.select(2)
            if not ready:
                print(f"no connections right now, total {selector.total_clients}, max {selector.max_clients}")
                continue
            for sel_key, _ in ready:
                sock = sel_key.fileobj
                if sock is server_socket:
                    accept_conn(sock, selector)
                else:
                    try:
                        send_response(sock)
                    except socket.error as exc:
                        print(f'Error receiving data: {exc}')
                        sock.close()
                        selector.unregister(sock)


def server() -> None:
    print('Server start')
    server_socket = create_server(address)
    event_loop(server_socket)
    print('Server shutdown')


class Client(threading.Thread):
    def __init__(self):
        super().__init__()
        self.ok = 0

    def run(self):
        client_sock = socket.socket()
        client_sock.connect(address)
        for n in range(REQUESTS):
            t1 = perf_counter()
            client_sock.send('1 2 3 4 5 6 7'.encode())
            response = client_sock.recv(1024)
            t2 = perf_counter()
            print(f"Response from server: {response.decode()}, {t2 - t1}")
            sleep(0.01)
        client_sock.close()
        self.ok = 1


def client() -> None:
    tasks = []
    for n in range(CLIENTS):
        task = Client()
        task.start()
        tasks.append(task)
        sleep(0.001)  # иначе при одновременном подключении всех клиентов треть отваливается с ConnectionRefusedError
    for task in tasks:
        task.join()
    print('stat', CLIENTS, sum(t.ok for t in tasks))


if __name__ == "__main__":
    address = ("localhost", 5555)
    try:
        with socket.socket() as check:
            check.connect(address)
    except ConnectionRefusedError:
        server()
    else:
        client()
