
def vowels_finding(s):
    vow="aeiou"
    c=0
    v=0
    l=[]
    l2=[]
    l3=[]
    end=len(s)
    begin=0
    for a in range(len(s)):
        if s[a] not in vow:
            #print(s[a])
            c=c+1
            #print(c)
            l.append(s[a])
            #print('not vowels',l)
            #print('dup',l2)
            #final=s.find(s[a])
            #print('vowels postition found at',final)
            #print(l)
        else :
            l3.append(s[a])
            print(s[a],s.count(s[a]))
            o=s.find(s[a])
            #print(o)
            #print('vowels',l3)
            
            #j=j+1
            #print('not vowels',s[a],j)
vowels_finding('hello')
    
#f=s.index(t)
        #l.append(f)
        #print('  ',f)
        #print(' ',l)
        
