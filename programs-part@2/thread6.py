import threading
import time
class X(threading.Thread):
    def run(self):
        for p in range(1,101):
            #time.sleep(2)
            print(p)
class Y(threading.Thread):
    def run(self):
        time.sleep(3)
        for q in range(101,201):
            print(q)
x=X()
x.start()
y=Y()
y.start()
