from multiprocessing.connection import Client

address = ('localhost', 6001)  # адрес соединения со 2-м клиентом

with Client(address, authkey=b'password_2') as conn:
    while conn.poll(2):
        try:
            elem = conn.recv()
            print(f"client <- i={elem}")
            elem = f"{elem}B"  # клиент №2 модифицирует данные
            print(f"client -> i={elem}")
            conn.send(elem)
        except EOFError:
            print("CONNECTION CLOSED")
            break
