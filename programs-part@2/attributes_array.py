from numpy import *
a=array([1,2,3,4,5,6])
print('dimension',a.ndim)
b=array([[1,2,3],[4,5,6]])
print('dimension',b.ndim)
print('shape',a.shape)
print('shape',b.shape)  
print('reshape',b.reshape(3,2))
print('1 dimension',b.flatten())
print('size',a.size)
print('memory size',a.itemsize)
print('data type',a.dtype)
