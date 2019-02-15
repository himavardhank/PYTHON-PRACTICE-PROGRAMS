import threading
import time
class X(threading.Thread):
    def run(self):
        time.sleep(10)
        self.sum=0
        for p in range(1,101):
            self.sum=self.sum+p
class Y(threading.Thread):
    def __init__(self,x1):
        super().__init__()
        self.x1=x1
    def run(self):
        for q in range(101,201):
            print(q)
            if q==150:
                self.x1.join()
                print(self.x1.sum)
x1=X()
x1.start()
y1=Y(x1)
print(y1)
y1.start()
