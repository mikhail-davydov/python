import random
import socket

from time import sleep


def client() -> None:
    client_sock = socket.socket()
    address = ("localhost", 5555)
    client_sock.connect(address)
    total = random.randint(20, 40)
    for i in range(total):
        sleep(1)
        client_sock.send(f"{i} {i}".encode())
        response = client_sock.recv(1024)
        print(f"Response from server: {response.decode()}, {total - 1 - i} left")
    client_sock.close()


if __name__ == "__main__":
    client()
