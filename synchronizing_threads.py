# Synchronizing_threads

import threading
import time

x = 8192

def double():
    global x
    while x < 16384:
        x *= 2
        time.sleep(1)
    print("reached the maximum")


def halve():
    global x
    while x > 1:
        x /= 2
        time.sleep(1)





