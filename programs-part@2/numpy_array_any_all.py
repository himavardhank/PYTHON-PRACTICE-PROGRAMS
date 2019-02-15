from numpy import *
a=array([1,2,3,0])
b=array([0,2,3,1])
c=a>b
print(c)
print('any function:',any(c))
print('all function:',all(c))
