import threading

def function():
    print('Hello World!')

t1 = threading.Thread(target=function)
t1.start()


 