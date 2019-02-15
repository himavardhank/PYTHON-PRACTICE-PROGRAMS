import threading 
class X(threading.Thread):
    def run(self):
        for p in range(1,101):
            print(p)
x=X()
x.start()
x1=X()
x1.start()
