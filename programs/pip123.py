import requests
url= 'https://api.speedcurve.com/v1/urls?days=1'
key= 'cn685aw5tj0i475zdzosbmtpslry82'
password ='Any_password'
response =requests.get(url,auth=(key,password))
d=(response.json())
print(d)
for k,v in d.items():
    #print(len(k))
    for p in v:
        print(p.get('site_id'))
