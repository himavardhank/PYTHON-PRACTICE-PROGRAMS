from numpy import *
a=reshape(arange(11,36,1),(5,5))
print(a)
print(a[:2,:3])
print(a[0:2,2:])
print(a[2:,3:])
for b in range(len(a)):
    for c in range(len(a[b])):
        print(a[b][c],end=' ')
