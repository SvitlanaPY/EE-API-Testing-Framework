from json.decoder import JSONDecodeError
from requests import Response
import json
class Assertions:

    @staticmethod
    def assert_json_value_by_name(response: Response, key_name, expected_value, error_message):
        assert response.status_code == 200, 'Wrong status code'
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in json format. Response text is {response.text}"

        assert key_name in response_as_dict, f"Response JSON doesn't have key {key_name}"
        assert response_as_dict[key_name] == expected_value, error_message
