# -*- coding: utf-8 -*-
import requests
import json
# rs=requests.get("http://127.0.0.1:7050/socalert_api/geteventrule?rule=A2",
# headers={'content-type':'application/json;charset=utf-8'})
# data=json.dumps(rs.json(),ensure_ascii=False)
# print(data)

rs=requests.get("http://127.0.0.1:7050/socalert/eventruledetail/?rule=A2",
headers={'content-type':'application/json;charset=utf-8'})
data=json.dumps(rs.json(),ensure_ascii=False)
print(data)