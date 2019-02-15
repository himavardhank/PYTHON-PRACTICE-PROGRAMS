class Emp:
    empcnt=0
    def __init__(self,ename,eadd,eid,esal):
        self.ename=ename
        self.eadd=eadd
        self.eid=eid
        self.esal=esal
        Emp.empcnt=Emp.empcnt+1
    def __del__(self):
        Emp.empcnt=Emp.empcnt-1
e1=Emp("scott","dallas",7788,3000.00)
e2=Emp("blake","colombo",7902,4000.00)
e3=Emp("smith","mumbai",7369,35000.00)
del e2
print("total no .of employees are:",Emp.empcnt)
