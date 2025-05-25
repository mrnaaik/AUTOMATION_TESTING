import requests
payload={"name":"Rama",
         "Job":"Software Engineer"}
resp=requests.put("https://reqres.in/api/users/2",data=payload)
print(resp.status_code)#200 status code as output if existing record updated
print(resp.json())
assert resp.json()["name"]=="Rama","NAME Mismatched"