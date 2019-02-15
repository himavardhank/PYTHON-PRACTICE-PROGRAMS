import csv
file=open('book.csv')
reader=csv.reader(file)
data=list(reader)
for line in data:
    print((line[0])
