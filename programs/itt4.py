x=[10,20,30,40]
it=iter(x)
while True:
    try:
        print(next(it))
    except(StopIteration):
        break
#for p in x:
#    print(p)
