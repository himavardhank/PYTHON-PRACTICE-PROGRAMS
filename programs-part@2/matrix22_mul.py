import sys
from numpy import *
r1,c1=[int(a)for a in input('enter 1st matrix size').split()]
r2,c2=[int(a)for a in input('enter 2nd matrix size').split()]
if c1!=r2:
    print('multiplictaion is not possible')
    sys.exit()
str1=input('enter 1st matrix ele')
x=reshape(matrix(str1),(r1,c1))
str2=input('enter 2nd matrix ele')
y=reshape(matrix(str2),(r2,c2))
z=x*y
print(z)
