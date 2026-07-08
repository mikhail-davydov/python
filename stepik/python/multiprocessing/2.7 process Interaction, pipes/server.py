from multiprocessing.connection import Listener
from random import uniform
from time import sleep

address_1 = ('localhost', 6000)  # адрес для первого соединения с клиентом №1
address_2 = ('localhost', 6001)  # адрес для второго соединения с клиентом №2

with Listener(address_1, authkey=b'password_1') as listener_1, \
        Listener(address_2, authkey=b'password_2') as listener_2:
    with listener_1.accept() as conn_1, listener_2.accept() as conn_2:
        print('connection 1 accepted from', listener_1.last_accepted)
        print('connection 2 accepted from', listener_2.last_accepted)
        for i in range(32):
            print(f"server -> i={i}")
            conn_1.send(i)
            conn_2.send(i)
            sleep(uniform(0, 1))
            print(f"server <- i={conn_1.recv()}")
            print(f"server <- i={conn_2.recv()}")

print("CONNECTION CLOSED")
