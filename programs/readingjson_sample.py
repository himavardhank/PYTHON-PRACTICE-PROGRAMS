import json
from pprint import pprint
json_file=open('F5_Week1.json')
d=json.load(json_file)
#pprint(d)
print(type(d))
l=len(d)
i=0
while i<=l:
    print(d[i])
    i+=1
    
#for a in d:
    #pprint(a)
    #for b in a:
#    if a[0].get('dow')=='Wednesday':
       #time=a[1].get('time')
       #for k,v in a[2].items():
           #l=v.get('Large')
           #print('large:',l,end='')
           #m=v.get('Medium')
           #print(" medium:",m,end='')
           #p=v.get('Phone Booth')
           #print(" phone:",p,end='')
           #s=v.get('Small')
           #print(" small:",s,end='')
           #print(l,m,p,s)
           #print(end='')
           #total=l+m+p+s
           #print('Wednesday:','time:',time,total)
#    else:
#        print('')
