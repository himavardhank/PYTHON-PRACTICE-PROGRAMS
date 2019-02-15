x={}
print(x)
print(type(x))
print(len(x))
y=dict()
print(type(y))
z={"java":90,"python":89,"hadoop":85}
print(z)
print(type(z))
p={"java":70,124.121:True,False:6+4j,"sr":"srt"}
print(p)
print(z.get(90))
print(z["python"])
print(p["java"])
print(p.get("java"))
z[True]=10101
print(z)
p["java"]=71
print(p)
k=p.items()
for v in k:
    print(v[0],v[1])
for r,q in z.items():
        print(r,q)
a={True:123,False:456,"abc":789}
for d in a:
    print(d,a[d])
l=a.keys()
for k in l:
    print(k)
print()

m=a.values()
for n in m:
    print(n)
print()
'hadoop' in z
