import json
json_file=open('java.json')
data=json.load(json_file)
lst=data['people']
for p in lst:
    print('name: '+p['name'])
    print('website: '+p['website'])
    print('from: '+p['from'])
