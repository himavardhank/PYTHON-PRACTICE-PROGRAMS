import test
import imp
b=2000
def f2():
    print("in f2 of demo")
print(b)
f2()
print("end")
imp.reload(test)
