import json
from pprint import pprint
json_file=open('F5_Week1.json')
d=json.load(json_file)
#pprint(d)
#print(type(d))
#print(len(d))
for a in d:
    #print(a)
    if a[1].get('time')=='14:00' & a[1].get('time')=='13:00':
        day=a[0].get('dow')
        #if a[2].get('conference-categories-count')=='Small':
        for k,v in a[2].items():
            l=v.get('Large')
            print('time:14:00',day,'large:',l)
            
    elif a[1].get('time')=='15:00' and a[1].get('time')=='09:00':
        day=a[0].get('dow')
        #if a[2].get('conference-categories-count')=='Small':
        for k,v in a[2].items():
            l=v.get('Large')
            print('time:14:00',day,'large:',l)
            
    elif a[1].get('time')=='10:00' and a[1].get('time')=='12:00':
        day=a[0].get('dow')
        #if a[2].get('conference-categories-count')=='Small':
        for k,v in a[2].items():
            l=v.get('Large')
            print('time:14:00',day,'large:',l)
            
    elif a[1].get('time')=='16:00' and a[1].get('time')=='11:00':
        day=a[0].get('dow')
        #if a[2].get('conference-categories-count')=='Small':
        for k,v in a[2].items():
            l=v.get('Large')
            print('time:14:00',day,'large:',l)
    else :
        print('')
            


    
    #if a[0].get('dow')=='Wednesday':
       #print('wednesday:','time:',a[1].get('time'),end=' ')
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
           #print(total,'\n')
                  
