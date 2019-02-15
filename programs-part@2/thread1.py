import threading 
class X(threading.Thread):
    def run(self):
        for p in range(1,101):
            print(p)
class Y(threading.Thread):
    def run(self):
        for q in range(101,201):
            print(q)
x=X()
x.start()
y=Y()
y.start()
