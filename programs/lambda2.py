add=lambda x,y:x+y
print (add(10,20))
sub=lambda x,y:x-y
print (sub(10,20))
mul=lambda x,y:x*y
print (mul(10,20))
a=lambda x,y:x+y*2
x=int(input("enter 1 num"))
y=int(input("enter 2 num"))
oper=raw_input("which opertaion do u want(1.add,2.sub,3.mul)")
if oper=='add':
    print(add(x,y))
else:
    print("sorry")
a(x,y)
