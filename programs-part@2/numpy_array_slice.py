from numpy import *
a=array(arange(10,16))
print(a)
print(a[1:6:2])
print(a[-2:2:-1])
print(a[:-2:])
i=0
while i<len(a):
    print(a[i])
    i+=1
