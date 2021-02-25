from selenium import webdriver
import requests
import json

def login():

    url = "http://givvy-api.projestic.com/api/v1/users/login"
    param_dict = {'email': 'yeyabed685@geeky83.com', 'password': 'Test123'}
    response = requests.post(url, data=(param_dict))
    response_body = response.json()
    assert response.status_code == 200
    response_name = response_body['data']['contact']['name']
    assert response_name == 'Ali Abdullaev'
    print(response.json())

login()


