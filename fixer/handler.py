import requests
import json


BASE_PATH = 'http://data.fixer.io/api/latest?access_key='

API_KEY = '7927af845b2f033bd3a40abd37e32aab'

url = BASE_PATH + API_KEY


def get_rate():

    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None