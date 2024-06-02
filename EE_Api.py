import requests

# parameters = {
#     'zipCode': '07450'
# #    'storeId': '24197'
# }
#
# headers_ = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjI5MTEsImlhdCI6MTY5ODg1NTM5NywibmJmIjoxNjk4ODU1Mzk3LCJleHAiOjE3MzAzOTEzOTd9.A8ns_cKXjPHcMupLeJddePhdkYhwStzmuwYSgwdG5FY"}
# response = requests.get("https://ee-api-sage.staging.inscyth.com/stores", params=parameters, headers=headers_)
#
# print(response.text)


import requests

parameters = {
    'zipCode': '07450'
}

headers_ = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjI5MTEsImlhdCI6MTY5ODg1NTM5NywibmJmIjoxNjk4ODU1Mzk3LCJleHAiOjE3MzAzOTEzOTd9.A8ns_cKXjPHcMupLeJddePhdkYhwStzmuwYSgwdG5FY"}
response = requests.get("https://ee-api-sage.staging.inscyth.com/zip-code/city", params=parameters, headers=headers_)

assert response.status_code == 200, 'Wrong status code'
assert 'city' in response.json(), "There is no city_parameter returned"
actual_city_value = response.json()['city']  # actual_cookie_value = response.cookies.get('HomeWork')
expected_city_value = 'Ridgewood'
assert actual_city_value == expected_city_value, 'Actual city_value is INcorrect'

assert response.status_code == 200, 'Wrong status code'
assert 'state' in response.json(), "There is no state_parameter returned"
actual_state_value = response.json()['state']  # actual_cookie_value = response.cookies.get('HomeWork')
expected_state_value = 'NJ'
assert actual_state_value == expected_state_value, 'Actual state_value is INcorrect'
