from json.decoder import JSONDecodeError
from requests import Response
# Response - це class в модулі requests

class BaseCase:

    def get_json_value(self, response: Response, key_name):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in json format. Response text is {response.text}"
        assert key_name in response_as_dict, f"Response JSON doesn't have key {key_name}"
        return response_as_dict[key_name]

