import threading
class X(threading.Thread):
    def run(self):
        print(self.getName())
class Y(threading.Thread):
    def run(self):
        print(self.getName())
x1=X()
x1.setName("X thread")
x1.start()
y1=Y()
y1.start()
