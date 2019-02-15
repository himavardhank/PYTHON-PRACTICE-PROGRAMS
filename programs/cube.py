def cube(a,func):
    p=func(a)
    return p*a
def square(b):
    return b*b
n=int((input("enter a number")))
n=cube(n,square)
print(n)
