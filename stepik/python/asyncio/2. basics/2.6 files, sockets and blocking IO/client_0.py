# Клиент

import socket


def client() -> None:
    client_sock = socket.socket()
    address = ("localhost", 5555)
    client_sock.connect(address)
    message = b"Hello from client!"
    client_sock.send(message)
    data = client_sock.recv(1024)
    print(f"Клиент получил ответ от сервера {data}")

    # в коде клиента хотим передать большое число:
    number = 299998866756
    data = number.to_bytes(8)  # <-- указываем 8 байт, т.к. передаем большое число
    client_sock.send(data)

    client_sock.close()


if __name__ == "__main__":
    client()