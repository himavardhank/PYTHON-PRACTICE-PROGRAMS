print("begin")
i=input("enter a +ve number")
x=int(i)
if x<10:
    print("given no is 1 digit number")
elif x<100:
    print("given num is 2 digit number")
elif x<1000:
    print("given num is 3 digit number")
else:
    print("given num is 4 digit number")
    print("end")
