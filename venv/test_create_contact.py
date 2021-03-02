import requests
import json
import random
import string
from random import randint
import pytest

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def test_create_contact():

    phone = '+38{}'.format(random_with_N_digits(7))
    newEmail = random_char(7) + "@gmail.com"
    url = "http://givvy-api.projestic.com/api/v1/contacts"
    headers = {"Authorization": "Bearer 3cc828bd49e868908b7d5892c3c38f5e16826ab9a5a724aeabd0cd96977784c7",
               "Content-Type": "application/json", "Accept": "application/json"}
    data_dict = {'first_name': 'Test', 'last_name': 'Tester', 'email': newEmail,
                 'mobile_phone': phone}
    create_contact_response = requests.post(url, json=(data_dict), headers=headers)
    status = create_contact_response.status_code
    print(str(status) + ' create contact test successful')
    body = create_contact_response.json()
    assert create_contact_response.status_code == 201
    user_id = body['data']['id']

test_create_contact()




