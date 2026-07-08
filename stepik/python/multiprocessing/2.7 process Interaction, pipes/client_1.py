from multiprocessing.connection import Client

address = ('localhost', 6000)  # адрес соединения с первым клиентом

with Client(address, authkey=b'password_1') as conn:
    while conn.poll(2):
        try:
            elem = conn.recv()
            print(f"client <- i={elem}")
            elem = f"{elem}A"  # клиент №1 модифицирует данные
            print(f"client -> i={elem}")
            conn.send(elem)
        except EOFError:
            print("CONNECTION CLOSED")
            break
