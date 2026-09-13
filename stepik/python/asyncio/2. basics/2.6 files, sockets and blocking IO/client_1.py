import socket


def client() -> None:
    with socket.socket() as client_sock:
        address = ("localhost", 5555)
        client_sock.connect(address)
        while (msg := input("Enter the numbers to calculate: ")) != "kill":
            client_sock.send(msg.encode())
            response = client_sock.recv(1024).decode()
            print(f"Response from server: {response}")

            if response == 'stop':
                print('server stopped')
                return


if __name__ == '__main__':
    client()
