import requests
import json
import random
import string
from random import randint

url = "http://givvy-api.projestic.com/api/v1/contacts"
headers = {"Authorization": "Bearer 3cc828bd49e868908b7d5892c3c38f5e16826ab9a5a724aeabd0cd96977784c7",
           "Content-Type": "application/json", "Accept": "application/json"}

def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def create_contact(phone, newEmail):

    data_dict = {'first_name': 'Test', 'last_name': 'Tester', 'email': newEmail,
                 'mobile_phone': phone}
    create_contact_response = requests.post(url, json=(data_dict), headers=headers)
    body = create_contact_response.json()
    assert create_contact_response.status_code == 201
    return body

def view_contact_created(user_id, body):

    view_contact_created_response = requests.get(url + '/' + str(user_id), headers=headers)
    assert view_contact_created_response.json() == body
    assert view_contact_created_response.status_code == 200

def delete_contact(user_id):

    delete_contact_response = requests.delete(url + '/' + str(user_id), headers=headers)
    status = delete_contact_response.status_code
    print('status ' + str(status) + ' delete test successful')
    assert delete_contact_response.status_code == 200

def view_contact_deleted(user_id):

    view_contact_deleted_response = requests.get(url + '/' + str(user_id), headers=headers)
    assert view_contact_deleted_response.status_code == 404

def test_end_to_end():

    phone = '+38{}'.format(random_with_N_digits(7))
    newEmail = random_char(7) + "@gmail.com"
    # create contact
    body = create_contact(phone, newEmail)
    # view created contact
    user_id = body['data']['id']
    view_contact_created(user_id, body)
    # delete contact
    delete_contact(user_id)
    # view deleted contact
    view_contact_deleted(user_id)

test_end_to_end()


