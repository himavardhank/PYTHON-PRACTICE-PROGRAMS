line="python language is a open source language"
words=line.split()
x=[[word.lower(),word.upper(),len(word)]
   for word in words]
for p in x:
 print(p)
