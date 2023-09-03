import requests
import pytest

BASE_URL = 'https://shefpovar63.ru/'
STATUS_OK = 200

def test_all_post():
    response = requests.get(BASE_URL)
    print(response.status_code)
    assert response.status_code == 200
    print(f'\n{response.headers}')
    # key = {'ID'}
    # assert key in response.headers.items()
