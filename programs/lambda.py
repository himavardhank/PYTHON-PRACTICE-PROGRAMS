x=[[1001,'book',200],[1002,'pen',500],[1004,'remote',600]]
x.sort(key=lambda p:p[0],reverse=False)
for p in x:
    print(p)
