from multiprocessing.managers import BaseManager

if __name__ == "__main__":
    m = BaseManager(address=('127.0.0.1', 50000), authkey=b'123')
    m.register('get_queue')
    m.connect()
    print("connect_ok")
    print(f"Client 2 successfully started")
    queue = m.get_queue()
    while True:
        result = queue.get()
        print(f"Клиент получил сообщение: {result}")
