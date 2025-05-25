#patch() method is used to update in individual field to be updated
import requests
payload={"job":"SDET"}
resp=requests.patch("https://reqres.in/api/users/2",data=payload)
print(resp.status_code)
print(resp.json())
assert resp.json()["job"]=="SDET","designation mismatched"