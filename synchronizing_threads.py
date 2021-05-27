# Synchronizing_threads
# Locking the resources

import threading
import time

x = 8192

lock = threading.Lock()                 # Locking 

def double():
    global x, lock
    lock.acquire()                      # Lock the resources for the thread
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("reached the maximum!")
    lock.release()                      # Releasing The Lock


def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print('Reached the minimum')
    lock.release()

t1 = threading.Thread(target = halve)
t2 = threading.Thread(target = double)

t1.start()
t2.start()




