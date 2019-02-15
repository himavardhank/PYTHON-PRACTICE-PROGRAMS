def my_gen():
    n=1
    print("this is printed first")
    yield n
    n+=1
    print("this is printed 2nd")
    yield n
    n+=1
    print("this is printed 3rd")
    yield n
it=my_gen()
while True:
    try:
        print(next(it))
    except(StopIteration):
        break
    
