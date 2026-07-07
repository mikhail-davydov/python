from sources import HandlerManager

if __name__ == "__main__":
    m = HandlerManager(address=('127.0.0.1', 50000), authkey=b'123')
    m.register('handler')
    m.connect()
    print("connect_ok")
    print(f"Client 1 successfully started")
    handler = m.handler()
    while text := input("Введите данные для расчета через пробел: "):
        data = map(float, text.split())
        handler.send(data)
