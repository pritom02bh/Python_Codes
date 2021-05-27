import threading

def function1():                            # Function One
    for x in range(10000):
        print('ONE')

def function2():                            # Function Two
    for x in range(10000):
        print('TWO')    

t1 = threading.Thread(target = function1)   # Thread one
t2 = threading.Thread(target = function2)   # Thread two

t1.start()
t2.start()