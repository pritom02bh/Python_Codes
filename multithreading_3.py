# Semaphores -->> to limit the access to the resources
# It doesn't lock the resources completely but limit them.

import threading
import time

semaphore = threading.BoundedSemaphore(value = 5)           # that allows only 5 accesses at a time

def access(thread_number):
    print("{} is trying to access!".format(thread_number))
    semaphore.acquire()
    print("{")
