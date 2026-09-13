# Сервер

import socket


def server() -> None:
    server_sock = socket.socket()
    address = ("localhost", 5555)
    server_sock.bind(address)
    server_sock.listen(1)
    conn, addr = server_sock.accept()
    data = conn.recv(1024)
    print(f"Сервер получил данные {data} от клиента с адресом {addr}")
    response = b'Hello from server!'
    print("и отправил ответ")
    conn.send(response)

    # в коде сервера декодируем обратно число в байты
    data = conn.recv(8)
    number = int.from_bytes(data)
    print(f"Получил число {number} от клиента с адресом {addr}")

    number_pow2 = number ** 2
    print(f'Квадрат числа {number} равен {number_pow2}')

    server_sock.close()


if __name__ == "__main__":
    server()
