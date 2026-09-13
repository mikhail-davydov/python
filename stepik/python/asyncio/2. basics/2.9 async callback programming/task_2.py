import selectors
import socket


def event_loop(server_socket: socket.socket) -> None:
    with selectors.DefaultSelector() as sel:
        sel.register(server_socket, selectors.EVENT_READ)
        while True:
            events = sel.select(2)
            if not events:
                print('Нет новых запросов за отведенный таймаут. Завершаем event_loop.')
                break
            for k, _ in events:
                sock: socket.socket = k.fileobj
                if sock is server_socket:
                    accept_conn(sock, sel)
                else:
                    try:
                        send_response(sock)
                    except socket.error as e:
                        print("Потеря связи с клиентом. Закрываем сокет, снимаем с регистрации.")
                        sock.close()
                        sel.unregister(sock)
