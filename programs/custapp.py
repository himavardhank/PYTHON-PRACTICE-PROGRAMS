class Cust:
    """cust app"""
    Cbname="sbi"
    def __init__(self,cname,caddre,cacno,cbal):
        self.cname=cname
        self.caddre=caddre
        self.cacno=cacno
        self.cbal=cbal
    def deposit(self,damt):
        self.cbal=self.cbal+damt
    def withdraw(self,wamt):
        self.wamt=self.cbal-wamt
    def dispaly(self):
        print(self.cname)
        print(self.caddre)
        print(self.cacno)
        print(self.cbal)
c1=Cust('hima','india',10002589,258976431000.000)
print(c1)
c1.deposit(20000)
c1.withdraw(0.2358)
c1.dispaly()
c2=Cust('himavardhan','india',10589469,14789976431000.000)
print(c1)
c2.deposit(204949600)
c2.withdraw(8)
c2.dispaly()
    
    
