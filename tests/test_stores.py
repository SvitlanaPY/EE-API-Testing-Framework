import pytest
import requests

class TestStores:
    parametersList = [
        ("07450"),
        ("77450"),
        ("47025")
        ]
    parametersList2 = [
        ("07450", '24197'),
        ("07450", '23633')
    ]

    def setup_method(self):
        self.headers_ = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjI5MTEsImlhdCI6MTY5ODg1NTM5NywibmJmIjoxNjk4ODU1Mzk3LCJleHAiOjE3MzAzOTEzOTd9.A8ns_cKXjPHcMupLeJddePhdkYhwStzmuwYSgwdG5FY"
        }

    @pytest.mark.parametrize('Zip_Code', parametersList)
    def test_get_five_stores(self, Zip_Code):
        response = requests.get("https://ee-api-sage.staging.inscyth.com/stores", params={'ZipCode': Zip_Code}, headers=self.headers_)
        assert response.status_code == 200, 'Wrong status code'

        response_as_dict = response.json()
        assert len(response_as_dict) <= 5, 'Returned stores are more than 5'


    @pytest.mark.parametrize('Zip_Code, Store_Id', parametersList2)
    def test_get_stores_by_StoreId(self, Zip_Code, Store_Id):
        response = requests.get("https://ee-api-sage.staging.inscyth.com/stores", params={'ZipCode': Zip_Code, 'storeId': Store_Id}, headers=self.headers_)
        assert response.status_code == 200, 'Wrong status code'

        response_as_dict = response.json()
        expected_adPatchId = response_as_dict[0]['adPatchId']
        for i in range(1, len(response_as_dict)):
            assert response_as_dict[i]['adPatchId'] == expected_adPatchId, f"Wrong adPatchId for {response_as_dict[i]['companyId']}"

        # for store in response_as_dict:
        #     assert store['adPatchId'] == expected_adPatchId, f"Wrong adPatchId for {store['companyId']}"
