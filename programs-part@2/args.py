def sum(*args,**kwargs):
    total=0
    for x in args:
        total=total+x
    print('sum',total)
sum(10)
sum()
sum(10,50)
sum(100,500,600)

def f1(**kwargs):
    for y in kwargs:
        pass
    print(kwargs)
f1(name='durga',rollno=101,marks=80,gf='sunny')
import os
print('filepath',__file__)
print('absolute path',os.path.abspath(__file__))
print('directory',os.path.dirname(os.path.abspath(__file__)))
basedir=os.path.dirname(os.path.abspath(__file__))
print(basedir)
temp=os.path.join(basedir,'templates')
print(temp)
