from time import sleep

from sources import HandlerManager

if __name__ == "__main__":
    m = HandlerManager(address=('127.0.0.1', 50000), authkey=b'123')
    m.register('handler')
    m.connect()
    print("connect_ok")
    print(f"Client 2 successfully started")
    handler = m.handler()
    while True:
        data = handler.get_data()
        if not data:
            sleep(0.5)
            continue
        print(f'\nСумма: {handler.get_sum()}')
        print(f'Произведение: {handler.get_mul()}')
        handler.clear()
