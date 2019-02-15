import requests
base_url="http://127.0.0.1:8000/"
end_url="jsondirectview"
r=requests.get(base_url+end_url)
data=r.json()
print("employee number:",data['eno'])
print("employee name:",data['ename'])
print("employee salray:",data['esal'])
print("employee adress:",data['eaddr'])


