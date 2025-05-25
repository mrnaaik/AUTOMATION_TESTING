#post() http request method
#post() method will upload the data means insert the data
import requests
payload={"name":"VENKAT",
         "job":"QA"}
resp=requests.post("https://reqres.in/api/users",data=payload)
print(resp.status_code)
print(resp.json())
assert resp.json()["job"]=="QA","Designation Mismatched"