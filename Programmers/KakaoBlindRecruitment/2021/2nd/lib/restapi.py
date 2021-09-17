import json
import requests
from requests.exceptions import HTTPError

class API:
    def __init__(self, endpoint, token):
        self.url = endpoint
        self.token = token
        self.auth_key = '6e0987b8-13f2-450e-8b6c-3e08a7bb1083'
        self.header = {'Authorization': '',
                       'Content-Type': 'application/json'}
        # self.header = {
        #     'Ocp-Apim-Subscription-Key': '8f89f23f3f284a1791ecf9ecf009887c',
        #     'Api-Access-Key': 'e3b11e4c-82d0-4f05-9c9b-31f9e9303481',
        #     'Content-Type': 'application/json'
        # }

    def get_start(self, senario):
        header = {'X-Auth-Token': self.token,
                       'Content-Type': 'application/json'}
        params = {'problem': senario}
        path = '/start'
        response = requests.post(self.url + path, headers=header, params=params)
        res = response.json()
        self.auth_key = res['auth_key']
        self.header['Authorization'] = self.auth_key

    def get(self, path):
        try:
            response = requests.get(self.url + path, headers=self.header)
            response.raise_for_status()
            jsonResponse = response.json()
            return jsonResponse

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def post(self, path, data):
        try:
            response = requests.post(self.url + path, headers=self.header, data=data)
            response.raise_for_status()
            jsonResponse = response.json()
            return jsonResponse
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def put(self, path, data):
        try:
            response = requests.put(self.url + path, headers=self.header, data=json.dumps(data))
            response.raise_for_status()
            jsonResponse = response.json()
            return jsonResponse
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')