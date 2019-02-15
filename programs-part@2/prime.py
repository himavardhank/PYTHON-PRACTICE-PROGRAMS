s,m=[int(a) for a in input('enter prime number range').split()]
for num in range(s,m+1):
    for i in range(2,num):
            if (num%i)==0:
                break
    else:
        print(num,end=' ')
