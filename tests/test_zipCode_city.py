import pytest
import requests
from lib.base_case import BaseCase

class TestCity(BaseCase):
    url = 'https://fd.staging.inscyth.com/api/zip-code/city'
    parametersList = [
        ("07450","Ridgewood","NJ"),
        ("77450","Katy","TX"),
        ("47025","Lawrenceburg","IN"),
        ("9255700","Moreno Valley","CA")
    ]
    parametersListNegative = [
        ("35001"),
        ("00000"),
        ("47o25"),
        ("")
        # ("77450")  # щоб негативний тест не пройшов, а впав з помилкою
    ]
    # def setup_method(self):
    #     self.headers_ = {
    #         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjI5MTEsImlhdCI6MTY5ODg1NTM5NywibmJmIjoxNjk4ODU1Mzk3LCJleHAiOjE3MzAzOTEzOTd9.A8ns_cKXjPHcMupLeJddePhdkYhwStzmuwYSgwdG5FY"
    #     }
    @pytest.mark.parametrize('ZIP_Code, expected_city, expected_state', parametersList)
    def test_city(self, ZIP_Code, expected_city, expected_state):
        response = requests.get(self.url, params={'zipCode': ZIP_Code})
        assert response.status_code == 200, 'Wrong status code'

        assert 'city' in response.json(), "There is no city_parameter returned"
        actual_city = response.json()['city']
        # self.actual_city = self.get_json_value(response, "city")
        assert actual_city == expected_city, 'Actual city_parameter is INcorrect'

        # assert 'state' in response.json(), "There is no state_parameter returned"
        # actual_state = response.json()['state']
        actual_state = self.get_json_value(response, "state")
        assert actual_state == expected_state, 'Actual state_parameter is INcorrect'


    @pytest.mark.parametrize('Zip_Code', parametersListNegative)
    def test_city_negative(self, ZIP_Code):
        response = requests.get(self.url, params={'zipCode': ZIP_Code})
        assert response.status_code == 404, 'Wrong status code'

