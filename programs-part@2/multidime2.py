from numpy import *
a=array(arange(1,10))
b=a.reshape(3,3)
#print(b)
for i in range(len(b)):
    print(b[i])
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j],end='')
