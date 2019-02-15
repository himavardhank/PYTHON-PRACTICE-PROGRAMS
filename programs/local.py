a=1000
b=2000
def f1():
    global a
    a=3000
    print(a)
    print(b)
def f2():
    print(a)
    print(b)
f1()
f2()
