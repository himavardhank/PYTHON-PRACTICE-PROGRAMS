print("begin")
a=input("enter 1st num")
b=input("enter 2nd number")
try:
    x=int(a)
    y=int(b)
    c=x/y
    print(c)
except(ZeroDivisionError):
        print("second number cant be zero")
except(ValueError):
    print("enter numeric value only")
except:
    print("error occured")  
print("end")
