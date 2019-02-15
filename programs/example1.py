import json
json_file=open('F5_Week1.json')
data=json.load(json_file)
lst=data[0:]
print(type(lst))
for a in lst:
   print(a)
print(type(a))
