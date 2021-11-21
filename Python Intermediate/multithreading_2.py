# make a function wait until the threads are complete.

import threading

def function1():
    for x in range(10):
        print('Executing Function One')

t1 = threading.Thread(target = function1)
t1.start()

t1.join()                         # Don't go for the next statement until the t1 thread is complete.cl


print("Hey People")
