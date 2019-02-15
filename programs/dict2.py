x={"java":{"spring":90,"structs":80},"python":{"django":95,"flask":80}}
print(x)
for k,v in x.items():
    print(k)
    for p,q in v.items():
        print(p,q)
