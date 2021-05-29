# Events and Daemon Threads

import threading

event = threading.Event()

def myfunction():
    print('Waiting for the event to trigger...\n')
    event.wait()
    print("performing action XYZ now...")

t1 = threading.Thread(target = myfunction)
t1.start

x = input("Do you want to trigger the event? (y/n) \n ")
if x == "y":
    event.set()
