from time import perf_counter

import random

import socket


def client() -> None:
    client_sock = socket.socket()
    address = ("localhost", 5555)
    client_sock.connect(address)
    # while (msg := input("Enter the numbers to calculate: ")) != "kill":
    r = random.randint
    counter = r(10, 30)
    while counter:
        msg = f'{r(1, 10)} {r(1, 10)} {r(1, 10)}'
        start = perf_counter()
        client_sock.send(msg.encode())
        response = client_sock.recv(1024)
        latency = perf_counter() - start
        counter -= 1
        print(f"Response from server: {response.decode()}, took: {latency}, left: {counter}")
    client_sock.close()


if __name__ == "__main__":
    client()
