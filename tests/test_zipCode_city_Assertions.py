import pytest
import requests
from lib.base_case import BaseCase
from lib.assertion import Assertions


class TestCity(BaseCase):
    parametersList = [
        ("07450", "Ridgewood", "NJ"),
        ("77450", "Katy", "TX"),
        ("47025", "Lawrenceburg", "IN"),
        ("9255700", "Moreno Valley", "CA")
    ]
    parametersListNegative = [
        ("35001"),
        ("00000"),
        ("47o25"),
        ("")
        # ("77450")  # щоб негативний тест не пройшов
    ]

    def setup_method(self):
        self.headers_ = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjI5MTEsImlhdCI6MTY5ODg1NTM5NywibmJmIjoxNjk4ODU1Mzk3LCJleHAiOjE3MzAzOTEzOTd9.A8ns_cKXjPHcMupLeJddePhdkYhwStzmuwYSgwdG5FY"
        }
    @pytest.mark.parametrize('Zip_Code, expected_city, expected_state', parametersList)
    def test_city(self, Zip_Code, expected_city, expected_state):

        # headers_ = {
        #     "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjI5MTEsImlhdCI6MTY5ODg1NTM5NywibmJmIjoxNjk4ODU1Mzk3LCJleHAiOjE3MzAzOTEzOTd9.A8ns_cKXjPHcMupLeJddePhdkYhwStzmuwYSgwdG5FY"}
        response = requests.get("https://ee-api-sage.staging.inscyth.com/zip-code/city", params={'zipCode': Zip_Code}, headers=self.headers_)

        Assertions.assert_json_value_by_name(
            response,
            "city",
            expected_city,
            "Actual city_parameter is INcorrect"
        )

        Assertions.assert_json_value_by_name(
            response,
            "state",
            expected_state,
            "Actual state_parameter is INcorrect"
        )


    @pytest.mark.parametrize('Zip_Code', parametersListNegative)
    def test_city_negative(self, Zip_Code):

        response = requests.get("https://ee-api-sage.staging.inscyth.com/zip-code/city", params={'zipCode': Zip_Code}, headers=self.headers_)
        assert response.status_code == 404, 'Wrong status code'
