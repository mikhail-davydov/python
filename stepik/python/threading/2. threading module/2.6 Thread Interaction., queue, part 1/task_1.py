import queue

first_queue = queue.Queue()
second_queue = queue.Queue()

while not first_queue.empty():
    second_queue.put(first_queue.get())
