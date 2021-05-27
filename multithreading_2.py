# make a function wait until the threads are complete.

import threading

def function1():
    for x in range(100):
        print('Executing Function One')

t1 = threading.Thread(target = function1)
t1.start()


print("Hey People")
