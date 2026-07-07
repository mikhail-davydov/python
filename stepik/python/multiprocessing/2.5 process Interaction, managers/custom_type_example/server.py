from sources import HandlerData, HandlerManager

if __name__ == "__main__":
    handler_data = HandlerData()

    manager = HandlerManager(address=("localhost", 50000), authkey=b"123")

    manager.register("handler", callable=lambda: handler_data)
    server = manager.get_server()
    print(f"server started")
    server.serve_forever()
