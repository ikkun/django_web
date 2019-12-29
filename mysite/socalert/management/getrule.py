import requests

headers = {'Content-Type':'application/x-www-form-urlencoded'}
dataAuthen={'username':'ikkun','password':'password123'}

url=r"http://127.0.0.1:7050/api/token/"

rs=requests.post(url,data=dataAuthen,headers=headers).json()
token = rs['access']
print(token)
rs=requests.get("http://127.0.0.1:7050/socalert_api/geteventrule?rule=A2")
print(rs.json())