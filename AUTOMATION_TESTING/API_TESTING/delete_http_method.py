import requests
import pytest
class Test_delete:
    def test_delete_api_endpoint(self):
        resp=requests.delete("https://reqres.in/api/users/2")
        print(resp.status_code) #if the record successfully deleted 204 is status code
        assert resp.status_code==204,"Deletion Failed"