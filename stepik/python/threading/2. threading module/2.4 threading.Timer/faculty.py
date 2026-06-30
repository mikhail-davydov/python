import datetime
import threading

start_timer = False
input_cycle = True


def timer_func():
    if not start_timer:
        return
    print(datetime.datetime.now())
    timer = threading.Timer(interval=1, function=timer_func)
    timer.daemon = True
    timer.start()


while input_cycle:
    command = input()
    if command == 'start':
        start_timer = True
        timer_func()
    elif command == 'stop':
        start_timer = False
    elif command == 'exit':
        input_cycle = False
    else:
        print('incorrect input')
