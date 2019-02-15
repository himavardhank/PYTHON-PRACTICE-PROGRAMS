import json
from pprint import pprint
json_file=open('F5_Week1.json')
d=json.load(json_file)
#pprint(d)
#print(type(d))
#print(len(d))
for a in d:
    #pprint(a)
    #for b in a:
    if a[0].get('dow')=='Wednesday':
       print('wednesday:','time:',a[1].get('time'),end=' ')
       for k,v in a[2].items():
           l=v.get('Large')
           #print('large:',l,end='')
           m=v.get('Medium')
           #print(" medium:",m,end='')
           p=v.get('Phone Booth')
           #print(" phone:",p,end='')
           s=v.get('Small')
           #print(" small:",s,end='')
           #print(l,m,p,s)
           #print(end='')
           total=l+m+p+s
           print(total,'\n')
    elif a[0].get('dow')=='Thursday':
        print('Thursday:','time:',a[1].get('time'),end=' ')
        for k,v in a[2].items():
           l=v.get('Large')
           #print('large:',l,end='')
           m=v.get('Medium')
           #print(" medium:",m,end='')
           p=v.get('Phone Booth')
           #print(" phone:",p,end='')
           s=v.get('Small')
           #print(" small:",s,end='')
           #print(l,m,p,s)
           #print(end='')
           total=l+m+p+s
           print(total)
    elif a[0].get('dow')=='Friday':
        print('Friday:','time:',a[1].get('time'),end=' ')
        for k,v in a[2].items():
           l=v.get('Large')
           #print('large:',l,end='')
           m=v.get('Medium')
           #print(" medium:",m,end='')
           p=v.get('Phone Booth')
           #print(" phone:",p,end='')
           s=v.get('Small')
           #print(" small:",s,end='')
           #print(l,m,p,s)
           #print(end='')
           total=l+m+p+s
           print(total)
    elif a[0].get('dow')=='Tuesday':
        print('Tuesday:','time:',a[1].get('time'),end=' ')
        for k,v in a[2].items():
           l=v.get('Large')
           #print('large:',l,end='')
           m=v.get('Medium')
           #print(" medium:",m,end='')
           p=v.get('Phone Booth')
           #print(" phone:",p,end='')
           s=v.get('Small')
           #print(" small:",s,end='')
           #print(l,m,p,s)
           #print(end='')
           total=l+m+p+s
           print(total)
    elif a[0].get('dow')=='Monday':
        print('Monday:','time:',a[1].get('time'),end=' ')
        for k,v in a[2].items():
           l=v.get('Large')
           #print('large:',l,end='')
           m=v.get('Medium')
           #print(" medium:",m,end='')
           p=v.get('Phone Booth')
           #print(" phone:",p,end='')
           s=v.get('Small')
           #print(" small:",s,end='')
           #print(l,m,p,s)
           #print(end='')
           total=l+m+p+s
           print(total)
    else:
        print(end="")
            



            #print(a[2].get('conference-categories-count'))
    


        
        #print(a[0].get('dow'))



        #if a[0].get('get')=='Thursday':
            #print(a[0].get('dow'))
    
            
    #if a[0]=='Wednesday':
        #print("ok")
        #print("wednesday:",a[1].get('time'))
    #print("week:",a[0].get('dow'),"time:",a[1].get('time'))
    #for k,v in a[2].items():
      #  v1=v.values()

        
