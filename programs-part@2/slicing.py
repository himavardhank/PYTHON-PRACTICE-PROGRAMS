from numpy import *
a=array(arange(1,10))
b=a.reshape(3,3)
print(b)
print('for rows',b[0,:])
print(b[1,:])
print(b[2,:])
print('for  1st column',b[:,0])
print('for 2nd column',b[:,1])
print('for 3rd column',b[:,2])