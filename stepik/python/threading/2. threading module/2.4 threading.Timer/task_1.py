msg = ...


def my_function(msg):
    pass


import threading

my_timer = threading.Timer(interval=1, function=my_function, args=[msg])
my_timer.name = 'MyTimer'
my_timer.daemon = True

