from numpy import *
a=arange(1,6)
b=a
print('a:',a)
print('b:',b)
b[0]=99
print('after adding ele into alias:',b)
print(a)
c=arange(1,11)
d=c.view()
print('before view',c)
print(d)
c[0]=100
print('after adding ele into view of c:',c)
print(d)
e=arange(100,110)
f=e.copy()
print('before copy',e)
print(f)
e[0]=200
f[5]=500
print('after copy',e)
print('does not effect to its copy',f)

