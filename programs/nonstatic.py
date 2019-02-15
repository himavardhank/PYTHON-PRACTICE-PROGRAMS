class Demo:
    """non static variables"""
    def insert(self):
        self.a=1000
        self.b=2000
    def display(self):
        print(self.a)
        print(self.b)
t=Demo()
t.insert()
t.display()
print(t.a)
print(t.b)
