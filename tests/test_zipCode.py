import pytest
import requests
# from lib.base_case import BaseCase

# In summary for the US:
# Latitude: [−14.34, +71.39]
# Longitude: [−179.9, +172.44]

class TestZipCode():
    retailer_url = "https://fd.staging.inscyth.com/api/zip-code"
    parametersList = [
        ("39.182648106851005", "-84.8552564674385", "47025"),
        ("29.7654421122147", "-95.74277876137626", "77450")
    ]

    # def setup_method(self):
    #     self.headers_ = {
    #         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjI5MTEsImlhdCI6MTY5ODg1NTM5NywibmJmIjoxNjk4ODU1Mzk3LCJleHAiOjE3MzAzOTEzOTd9.A8ns_cKXjPHcMupLeJddePhdkYhwStzmuwYSgwdG5FY"
    #     }
    @pytest.mark.parametrize('lat, long, expected_zipCode', parametersList)
    def test_zipCode(self, lat, long, expected_zipCode):
        response = requests.get(self.retailer_url, params={'latitude': lat, 'longitude': long})
        assert response.status_code == 200, 'Wrong status code'

        actual_zipCode = response.text
        assert actual_zipCode == expected_zipCode, 'Actual zipCode_parameter is INcorrect'

