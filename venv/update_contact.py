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
    print(create_contact_response.json())
    body = create_contact_response.json()
    assert create_contact_response.status_code == 201
    return body

def update_contact(user_id, newEmail):
    updated_data = {'first_name': 'Ali', 'last_name': 'Abdullaiev', 'email': newEmail}
    update_contact_response = requests.patch(url + '/' + str(user_id), json=(updated_data), headers=headers)
    assert update_contact_response.status_code == 200
    contact_info = update_contact_response.json()
    print(contact_info)
    assert contact_info['data']['first_name'] == 'Ali'

def delete_contact(user_id):
    delete_contact_response = requests.delete(url + '/' + str(user_id), headers=headers)
    print(delete_contact_response.json())
    print(delete_contact_response.status_code)
    assert delete_contact_response.status_code == 200

def update_contact_test():
    phone = '+38{}'.format(random_with_N_digits(7))
    newEmail = random_char(7) + "@gmail.com"
    # create contact
    body = create_contact(phone, newEmail)
    user_id = body['data']['id']
    # update contact
    update_contact(user_id, newEmail)
    # delete contact
    delete_contact(user_id)

update_contact_test()