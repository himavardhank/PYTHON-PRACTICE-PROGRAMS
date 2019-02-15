import Json
data={}
data['people']=[]
data['people'].append({'name':'scott','website':'facebook.com','from':'nebraska'})
data['people'].append({'name':'larry','website':'google.com','from':'michigan'})
data['people'].append({'name':'tim','website':'apple.com','from':'alabama'})
with open('data.Json','w')as outfile:son.dump(data,outfile)
