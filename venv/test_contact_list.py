import requests
import json
import pytest

def test_contact_list():

    url = "http://givvy-api.projestic.com/api/v1/contacts"
    headers = {"Authorization": "Bearer 3cc828bd49e868908b7d5892c3c38f5e16826ab9a5a724aeabd0cd96977784c7",
               "Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response_body = response.json()
    status = response.status_code
    print(str(status) + ' contact list test successful')
    assert response.status_code == 200

test_contact_list()


