import multiprocessing
from multiprocessing.managers import BaseManager
from queue import Queue


class QueueManager(BaseManager):
    pass


if __name__ == "__main__":
    queue = Queue()

    manager = QueueManager(address=("localhost", 50000), authkey=b"123")
    manager.register("get_queue", callable=lambda: queue)
    server = manager.get_server()
    pr_name = multiprocessing.current_process().name
    pr_pid = multiprocessing.current_process().pid
    print(f"server started with {pr_name}, process PID = {pr_pid}")
    server.serve_forever()
