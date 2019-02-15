class Valuetoosmallerror(Exception):
    pass
class Valuetoolargeerror(Exception):
    pass
number=10
while True:
    try:
        i=int(input("enter a number"))
        if i<number:
            raise Valuetoosmallerror
        elif i>number:
            raise Valuetoolargeerror
        break
    except(Valuetoosmallerror):
        print("this value is too small,try again!")
    except(Valuetoolargeerror):
        print('this value is too large ,try again!')
print("congrats you guessed it correctly")
