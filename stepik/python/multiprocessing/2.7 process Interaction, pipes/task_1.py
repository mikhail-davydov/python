from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection


def sender(conn: Connection) -> None:
    message = "Hello from sender!"
    number = 42
    float_number = 3.14159
    with conn:
        for data in (message, number, float_number, bytearray(message.encode()) + bytearray(number.to_bytes(4, byteorder='big'))):
            conn.send(data)


if __name__ == "__main__":
    recv_conn, send_conn = Pipe(duplex=False)
    p = Process(target=sender, args=[send_conn])
    p.start()
    p.join()
    recv_data = []
    while recv_conn.poll():
        recv_data.append(recv_conn.recv())
    print(recv_data)