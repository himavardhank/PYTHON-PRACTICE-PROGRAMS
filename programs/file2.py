x=open("myfile.txt")
print(x.tell())
x.seek(4)
print(x.tell())
print(x.read())
print(x.tell())
x.close()
