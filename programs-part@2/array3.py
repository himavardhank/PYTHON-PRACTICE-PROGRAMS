from array import *
a=array('i',[1,2,3,4])
#methods in array
a.append(5) 
a.insert(0,0)
print(a.remove(5))
a.remove(0)
print(a.pop())
print(a.index(1))
lst=a.tolist()
print(type(lst))
for b in a:
    print(b,end=' ')
