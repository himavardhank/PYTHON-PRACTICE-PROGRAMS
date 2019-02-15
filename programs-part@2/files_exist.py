import os,sys
fname=input('file name')
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname+'not exist')
    sys.exit()
print('the file content are')
str=f.read()
print(str)
f.close()
