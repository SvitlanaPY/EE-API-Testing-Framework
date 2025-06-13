import pytest
import requests
import json


class TestStores:
    # storesMaxQty_Parameters = [['https://fd.staging.inscyth.com/api/stores', '07450', 6], ['https://lowes.staging.inscyth.com/api/stores', '07450', 5]]
    # storesQty_byStoreId_Parameters = [['https://fd.staging.inscyth.com/api/stores', '07450', 22788]]

    test_parameters = {
        "storesMaxQty_Parameters": [['https://fd.staging.inscyth.com/api/stores', '07450', 6], ['https://lowes.staging.inscyth.com/api/stores', '07450', 5]],
        "storesQty_byStoreId_Parameters": [['https://fd.staging.inscyth.com/api/stores', '07450', 22788]]
    }

    @pytest.mark.parametrize('retailer_url, ZIP_Code, StoresQty', test_parameters['storesMaxQty_Parameters'])
    def test_storesMaxQty(self, retailer_url, ZIP_Code, StoresQty):

        response = requests.get(retailer_url, params={'zipCode': ZIP_Code})
        assert response.status_code == 200, 'Wrong status code'

        response_dict = response.json()
        assert len(response_dict) == StoresQty, 'Wrong quantity of the closest stores'

    @pytest.mark.parametrize('retailer_url, ZIP_Code, Store_Id', test_parameters['storesQty_byStoreId_Parameters'])
    def test_storesQty_byStoreId(self, retailer_url, ZIP_Code, Store_Id):
        # expected_adPatch: str = 'null'
        response = requests.get(retailer_url, params={'zipCode': ZIP_Code, 'storeId': Store_Id})
        assert response.status_code == 200, 'Wrong status code'

        response_dict = response.json()
        for stores in response_dict:
            if stores['companyId'] == Store_Id:
                expected_adPatch = stores['adPatchId']
                break
        for elem in response_dict:
            assert elem['adPatchId'] == expected_adPatch, 'Wrong adPatch code'

