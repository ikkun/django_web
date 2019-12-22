import requests

headers = {'Content-Type':'application/x-www-form-urlencoded'}
dataAuthen={'username':'ikkun','password':'password123'}

url=r"http://127.0.0.1:7050/api/token/"

rs=requests.post(url,data=dataAuthen,headers=headers).json()
token = rs['access']


data_ingest={
    'types':'Sec',
    'title':'ทดสอบ alert 3',
    'description':'รายละเอียด alert',
    'severity':1,
    'contact':'แอดมิน'
}

rs=requests.post("http://127.0.0.1:7050/socalert_api/eventalert/",
    data=data_ingest,
    headers={"Authorization":"Bearer {}".format(token)})
print(rs.json())