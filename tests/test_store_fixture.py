import pytest
import requests
import json

class TestStores:

    def test_storesMaxQty(self, test_params_stores_max_qty):
        """
        Тест використовує фікстуру test_params_stores_max_qty для отримання параметрів.
        """
        retailer_url, ZIP_Code, StoresQty = test_params_stores_max_qty

        response = requests.get(retailer_url, params={'zipCode': ZIP_Code})
        assert response.status_code == 200, 'Wrong status code'

        response_dict = response.json()
        assert len(response_dict) == StoresQty, 'Wrong quantity of the closest stores'

    def test_storesQty_byStoreId(self, test_params_stores_qty_by_store_id):
        """
        Тест використовує фікстуру test_params_stores_qty_by_storeId для отримання параметрів.
        """
        retailer_url, ZIP_Code, Store_Id = test_params_stores_qty_by_store_id

        response = requests.get(retailer_url, params={'zipCode': ZIP_Code, 'storeId': Store_Id})
        assert response.status_code == 200, 'Wrong status code'

        response_dict = response.json()
        for stores in response_dict:
            if stores['companyId'] == Store_Id:
                expected_adPatch = stores['adPatchId']
                break
        for elem in response_dict:
            assert elem['adPatchId'] == expected_adPatch, 'Wrong adPatch code'

