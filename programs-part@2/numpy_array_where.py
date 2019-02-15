from numpy import *
a=array(arange(1,6))
b=array([1,0,5,11,6])
c=where(a>b,a,b)
print(c)
d=array([1,2,0,-1,0,6],int)
e=nonzero(d)
print(e)
for i in e:
    print(i)

