from array import *
a=array('i',[5,6,7,8])
for ele in a:
    print(ele)
array1=array('d',[1.5,2.5,3.5,4.5])
array2=array(array1.typecode,(a*3 for a in array1))
for i in array2:
    print('elements are:',i)
