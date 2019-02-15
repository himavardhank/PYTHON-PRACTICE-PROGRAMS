import json
from pprint import pprint
json_file=open('feed.json')
data=json.load(json_file)
x=data
#pprint(x)
#print(json.dumps(data,indent=2))
y=x["near_earth_objects"]["2015-09-07"]
pprint(y)



