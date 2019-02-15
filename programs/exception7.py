try:
    print("in try 1")
    try:
        print("in try 2")
    except(ZeroDivisionError):
         print("in except 2")
    finally:
        print("in finally 2")
except(ValueError):
    print("in except1")
    try:
        print("in try 3")
    except(KeyError):
        print("in except3")
    finally:
        print("in finally 3")
finally:
    print('in finally 1')
    try:
        print("in try 4")
    except(IndexError):
         print("in except 4")
    finally:
        print("in finally 4")
    
