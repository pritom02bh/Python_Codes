import threading

def helloworld():
    print('Hello World!')

t1 = threading.Thread(target=helloworld)
t1.start()


 