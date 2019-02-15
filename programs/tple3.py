x=(10,20,30,40,50,10,20,70)
print(x)
print(x.count(10))
print(x.count(70))
print(x.index(70))
print(x.index(10,3))
y=((10,20,30),(40,50,60),(70,80,90))
for p in y:
    print(p, type(p))


y1=((10,20,30),(40,50,60),(70,80,90))
for p in y1:
    for q in p:
        print(q,end=" ")
    print()
for a,b,c in y1:
    print(a,b,c)
