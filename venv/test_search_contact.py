import requests
import json

def test_search_contact():

    url = "http://givvy-api.projestic.com/api/v1/contacts"
    headers = {"Authorization": "Bearer 3cc828bd49e868908b7d5892c3c38f5e16826ab9a5a724aeabd0cd96977784c7",
               "Content-Type": "application/json", "Accept": "application/json"}
    params = {'query': 'Ali'}
    search_contact_response = requests.get(url, params=params, headers=headers)
    status = search_contact_response.status_code
    print('status ' + str(status) + ' search test successful')
    assert search_contact_response.status_code == 200


test_search_contact()


