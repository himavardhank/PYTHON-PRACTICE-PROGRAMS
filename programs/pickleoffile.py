import pickle
data=[['scott',7788,3000.00],[
    'blake',7902,4000.0],
      ['smith',7309,5000.00]]
x=None
try:
    x=open('picfile.txt','wb')
    print("file is opened")
    pickle.dump(data,x)
except:
        print("error occured")
finally:
        if x!=None:
            x.close()
            print("file is closed")
