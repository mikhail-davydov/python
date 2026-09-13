# ----------------------------------------------------------
# server.py
# ----------------------------------------------------------
# Сервер принимает и обрабатывает данные от клиента
# Клиент передает строковое сообщение, содержащее несколько
# целых чисел, разделенных между собой пробелами, например
# "11 345 23 11902 23"
# Сервер возвращает сумму этих чисел
# Сервер может принимать несколько соединений одновременно
# Используется модуль threading
# ----------------------------------------------------------

import logging
import socket
import threading
from typing import Callable, Optional


class SocketServerError(Exception):
    """Базовое искючение для ошибок сервера"""
    pass


class DataError(SocketServerError):
    """Исключение для некорректных данных от клиента"""
    pass


class ClientThread(threading.Thread):
    """
    Класс представляет поток обработки клиентского соединения.

    Атрибуты:
        client_socket  - клиентский сокет, полученный сервером
                         при принятии соединения
        client_address - адрес клиента, который соединился с сервером
        data_handler   - функция, которая обрабатывает данные полученные
           от клиента и переданные в качестве параметра
           и возвращает результат типа int
           В случае получения некорректных данных - бросает исключение DataError
    """

    def __init__(
            self,
            client_socket: socket.socket,
            client_address: tuple[str, int],
            data_handler: Callable[[bytes], int],
            stop_event: threading.Event,
    ) -> None:
        super().__init__()
        self.client_socket = client_socket
        self.client_address = client_address
        self._data_handler = data_handler
        self._stop_event = stop_event

    def run(self):
        logging.info(
            f"Новое соединение от {self.client_address}",
        )
        try:
            # Предполагаем поток данных от клиента в
            # рамках одного соединения ...
            while not self._stop_event.is_set():
                data = self.client_socket.recv(1024)
                if not data:
                    break

                try:
                    # обработка полученных данных данных
                    result = self._data_handler(data)

                    # Отправляем результат клиенту ...
                    self.client_socket.send(
                        result.to_bytes(8),
                    )
                except DataError as e:
                    # некорректные данные от клиента
                    # игнорируем и идем за следующей порцией...
                    logging.error(f"Ошибка данных: {e}")
                    continue

        except ConnectionResetError:
            logging.info(
                f"Клиент {self.client_address} разорвал соединение",
            )
        finally:
            self.client_socket.close()
            logging.info(
                f"Соединение с {self.client_address} закрыто",
            )


class SocketServer:
    """
    Класс представляет socket-сервер, обрабатывающий поток клиентских
    данных определенного формата (строка чисел) и возвращающий клиенту результат (сумму этих чисел).

    Атрибуты:
        address - адрес
        port    -  порт
        backlog - количество одновременных соединений
        handler - функция, которая обрабатывает данные полученные
           от клиента и переданные в качестве параметра
           и возвращает результат типа int
           В случае получения некорректных данных - бросает исключение DataError
    """

    def __init__(
            self,
            address: str,
            port: int,
            backlog: int,
            handler: Callable[[bytes], int],
    ) -> None:
        self.address = address
        self.port = port
        self.backlog = backlog
        self.handler = handler

        self._sock: Optional[socket.socket] = None
        self._create_socket()
        self._clients: list[ClientThread] = []
        self._stop_event: threading.Event = threading.Event()

    def _create_socket(self) -> None:
        """Создание и настройка сокета"""

        try:
            self._sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM,
            )
            self._sock.setsockopt(
                socket.SOL_SOCKET,
                socket.SO_REUSEADDR,
                1,
            )
        except socket.error as e:
            raise SocketServerError(
                f"Ошибка создания серверного сокета: {e}",
            )

    def run(self) -> None:
        """Запуск сервера"""

        if not self._sock:
            raise SocketServerError("Серверный сокет не инициирован")
        try:
            self._sock.bind((self.address, self.port))
            self._sock.listen(self.backlog)
            logging.info(
                f"Сервер стартует по адресу {self.address}:{self.port}",
            )
            while True:
                # Цикл приема и обработки соединений ...
                try:
                    conn, addr = self._accept_connection()
                    logging.info(f"Принят запрос на соединение от {addr}")

                    # создание потока обработки соединения
                    self._clients.append(
                        new_thread := ClientThread(
                            conn, addr,
                            self.handler,
                            self._stop_event,
                        ),
                    )
                    new_thread.start()

                except ConnectionError as e:
                    logging.error(f"Ошибка соединения с клиентом: {e}")
                    continue
        except socket.error as e:
            raise SocketServerError(f"Ошибка сервера: {e}")
        finally:
            self._close_socket()

    def close(self) -> None:
        # останавливаем server

        self._stop_event.set()
        for thread in self._clients:
            thread.join()
        self._close_socket()

    def _accept_connection(self) -> tuple[socket.socket, tuple[str, int]]:
        """Принятие клиентского соединения"""

        if not self._sock:
            raise SocketServerError("Серверный сокет не инициирован")
        try:
            return self._sock.accept()
        except socket.error as e:
            raise ConnectionError(f"Ошибка принятия соединения: {e}")

    def _close_socket(self) -> None:
        """Закрытие серверного сокета"""

        if self._sock:
            try:
                self._sock.close()
            except socket.error as e:
                logging.error(f"Ошибка закрытия сокета: {e}")


# ----------------------------------------------------------

def handler(data: bytes) -> int:
    """Обработк клиентских данных"""

    try:
        result = sum(map(int, data.decode().split()))
        return result
    except ValueError as e:
        logging.error(f"Некорректные данные от клиента: {e}")
        raise DataError(f"Некорректные данные: {e}")


# ----------------------------------------------------------
def server() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )
    try:
        socket_server = SocketServer('127.0.0.1', 5555, 1, handler)
        socket_server.run()
    except SocketServerError as e:
        logging.error(f"Server error: {e}")
    except KeyboardInterrupt:
        logging.info("Сервер остановлен пользователем.")
    finally:
        socket_server.close()
        logging.info("Сервер закрыт.")


# ==========================================================

if __name__ == '__main__':
    server()
