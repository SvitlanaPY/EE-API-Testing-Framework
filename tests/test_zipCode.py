import pytest
import requests
# from lib.base_case import BaseCase

class TestZipCode():
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
        url = 'https://fd.staging.inscyth.com/api/zip-code'
        response = requests.get(url, params={'latitude': lat, 'longitude': long})
        assert response.status_code == 200, 'Wrong status code'
        self.actual_zipCode = response.text
        assert self.actual_zipCode == expected_zipCode, 'Actual zipCode_parameter is INcorrect'
