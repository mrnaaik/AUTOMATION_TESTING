import requests
import pytest
#get() method http based method which is used to read data from the desired api endpoint
#apply get() method to get data from api end point
class Test_api:
    def test_status_code_check(self):
        api_ref=requests.get("https://reqres.in/api/users?page=2")
        print(api_ref.status_code)
        d=api_ref.json()
        #print(data)
        assert api_ref.status_code==200,"API END POINT IS not reachable"
    def test_name_validation(self):
        res = requests.get("https://reqres.in/api/users?page=2")
        d=res.json() #this line obtain data from the api end point and assign to the d an object
        assert d["data"][0]["first_name"]=="Michael","NAME is mismatched"


    def test_email_validation(self):
        res = requests.get("https://reqres.in/api/users?page=2")
        d=res.json()
        assert d["data"][0]["email"]=="michael.lawson@reqres.in","EMAIL MISMATCHED"
    def test_last_name_validatation(self):
        res = requests.get("https://reqres.in/api/users?page=2")
        d = res.json()
        assert d["data"][2]["last_name"]=="Funke","Last name mismatched"
