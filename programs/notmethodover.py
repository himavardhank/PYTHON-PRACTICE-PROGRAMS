class A:
    def add(self,instanceof,*args):
        if instanceof=='int':
            result=0
        if instanceof=='str':
            result=''
        for i in args:
            result=result+i
        print(result)
a=A()
#a.add('int',10,20,30)
a.add('str','lokeshit','python')
