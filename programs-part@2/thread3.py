import threading 
class X(threading.Thread):
    def run(self):
        myfunc()
class Y(threading.Thread):
    def run(self):
        myfunc()
def myfunc():
    for p in range(1,101):
        print(p)
x=X()
x.start()
y=Y()
y.start()
