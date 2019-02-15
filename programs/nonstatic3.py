class Demo:
    """non static variables"""
    def insert(self):
        self.a=1000
        self.b=2000
    def display(self):
        print(self.a)
        print(self.b)
        
d1=Demo()
d1.insert()
d1.display()
d2=Demo()
d2.display()
