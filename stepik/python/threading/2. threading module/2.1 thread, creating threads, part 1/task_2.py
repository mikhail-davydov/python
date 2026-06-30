import threading

tasks = []

for task in tasks:
    threading.Thread(target=task).start()