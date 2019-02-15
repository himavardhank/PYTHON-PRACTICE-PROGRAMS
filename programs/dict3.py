x={(20,10,30):[1,2,3],(40,50,60):(4,5,6),(70,80,90):{7,8,9}}
print(type(x))
for k,v in x.items():
    print(k,v)
print(len(x))
del dict[20]
print(x)
