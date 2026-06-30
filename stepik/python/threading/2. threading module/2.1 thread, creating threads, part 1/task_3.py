import threading

tasks = []
args = []

for i, task in enumerate(tasks):
    threading.Thread(target=task, args=(args[i],), name=task.__name__).start()

# alt

import threading

for task, arg in zip(tasks, args):
    threading.Thread(target=task, args=[arg], name=task.__name__).start()
