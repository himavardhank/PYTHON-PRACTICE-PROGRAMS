print("begin")
a=input("enter 1st num")
x=int(a)
b=input("enter 2nd number")
y=int(b)
try:
    c=x/y
    print(c)
except(ZeroDivisionError):
        print("second number cant be zero")
print("end")
