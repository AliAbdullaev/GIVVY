import pytest
import requests
import json

def test_login():

    url = "http://givvy-api.projestic.com/api/v1/users/login"
    param_dict = {'email': 'yeyabed685@geeky83.com', 'password': 'Test123'}
    response = requests.post(url, data=(param_dict))
    response_body = response.json()
    status = response.status_code
    print(str(status) + ' login test successful')
    assert response.status_code == 200
    response_name = response_body['data']['contact']['name']
    assert response_name == 'Ali Abdullaev'

test_login()


