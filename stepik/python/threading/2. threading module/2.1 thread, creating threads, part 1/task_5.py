import threading

tasks = []
kwargs = []

threads = [threading.Thread(target=task, kwargs=kw) for task, kw in zip(tasks, kwargs)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()