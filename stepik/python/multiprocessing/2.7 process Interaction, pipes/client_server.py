from multiprocessing import Process

import time
from multiprocessing.connection import Listener, Client


def run_server(backlog):
    address = ('localhost', 6000)
    with Listener(address, backlog=backlog) as listener:
        print(f"Сервер запущен с backlog={backlog}")
        for i in range(1, 6):  # Примем только 3 соединения
            conn = listener.accept()
            print(f"Принято соединение {i}")
            time.sleep(i)
            conn.send(f"Сообщение {i}")
            conn.close()


def run_client(client_id):
    address = ('localhost', 6000)
    try:
        conn = Client(address)
        print(f"Клиент {client_id} подключен\n", end="")
        print(conn.recv())
        conn.close()
    except Exception as e:
        print(f"Клиент {client_id} ошибка: {e}")


if __name__ == '__main__':
    backlog = 5
    server = Process(target=run_server, args=[backlog])
    server.start()
    clients = []
    for i in range(1, 6):
        clients.append(Process(target=run_client, args=[i]))
        clients[-1].start()
