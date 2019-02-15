from numpy import *
r,c=[int(a)for a in input('enter no.of rows and columns').split()]
str=input('enter elements into matrix')
x=reshape(matrix(str),(r,c))
print('your matrix',x)
y=x.transpose()
print("transpose",y)
