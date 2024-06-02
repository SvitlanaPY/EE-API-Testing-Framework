import pytest
import requests

class TestCity:
    parametersList = [
        ("07450","Ridgewood","NJ"),
        ("77450","Katy","TX"),
        ("47025","Lawrenceburg","IN")
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

        assert response.status_code == 200, 'Wrong status code'
        assert 'city' in response.json(), "There is no city_parameter returned"
        actual_city = response.json()['city']
        assert actual_city == expected_city, 'Actual city_parameter is INcorrect'

        assert response.status_code == 200, 'Wrong status code'
        assert 'state' in response.json(), "There is no state_parameter returned"
        actual_state = response.json()['state']
        assert actual_state == expected_state, 'Actual state_parameter is INcorrect'