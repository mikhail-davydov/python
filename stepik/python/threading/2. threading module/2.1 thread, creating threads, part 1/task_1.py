from time import sleep


def user_interface():
    while True:
        sleep(0.2)
        print("-", end="", flush=True)


def task():
    while True:
        sleep(0.61)
        print("*", end="", flush=True)


import threading

# Ваше решение
threading.Thread(target=user_interface).start()
threading.Thread(target=task).start()

# alt

threading.Thread(target=user_interface).start()
task()
