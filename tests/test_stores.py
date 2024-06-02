import pytest
import requests

class TestStores:
    #     parameters = [
    #         ("07450"),
    #         ("77450"),
    #         ("47025")
    #     ]
    parameters = {
        'zipCode': '07450'
        # 'storeId': '24197'
    }

    def setup_method(self):
        self.headers_ = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjI5MTEsImlhdCI6MTY5ODg1NTM5NywibmJmIjoxNjk4ODU1Mzk3LCJleHAiOjE3MzAzOTEzOTd9.A8ns_cKXjPHcMupLeJddePhdkYhwStzmuwYSgwdG5FY"
        }
    def test_stores(self):
        response = requests.get("https://ee-api-sage.staging.inscyth.com/stores", params=self.parameters, headers=self.headers_)
        assert response.status_code == 200, 'Wrong status code'
