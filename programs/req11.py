import json
from pprint import pprint
json_file=open('req1.json')
data=json.load(json_file)
x=data
pprint(x)
for y in x:
    pprint(y)
#print(json.dumps(data,indent=2))
