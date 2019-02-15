class Demo:
    """"non static variable"""
    def insert(self):
        self.a=1000
        self.b=2000
    def display(self):
        print(self.a)
        print(self.b)
    def modify(self):
        self.a=self.a+100
        self.b=self.b-100
d=Demo()
d.insert()
d.display()
d.modify()
d.display()
d1=Demo()
d1.insert()
d1.display()
d1.modify()
d1.display()
