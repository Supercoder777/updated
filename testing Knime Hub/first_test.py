import pytest
import requests
import json

def main_url():
    return "https://hub.knime.com"

def test_login_valid():
    url = "https://hub.knime.com/user/login?destination=/oauth2/authorize"

    data = {'email':'samuel4luve@yahoo.com','password':'zAddi623_'}

    response = requests.post(url, data=data)

    assert  response.status_code == 404