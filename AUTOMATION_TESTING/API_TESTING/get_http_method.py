import requests
#apply get() method to get data from api end point
api_ref=requests.get("https://reqres.in/api/users?page=2")
print(api_ref.status_code)
data=api_ref.json()
print(data)