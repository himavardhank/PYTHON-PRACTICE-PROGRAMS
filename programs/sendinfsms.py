import requests
mobno=input("enter mobile nummber")
msg=input("enter message")
res=requests.post('https://textbelt.com/text',{'phone':mobno,'message':msg,'key':'textbelt',})
result=res.json()
print(result)
