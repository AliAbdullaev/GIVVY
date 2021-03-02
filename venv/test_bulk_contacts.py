import pytest
import requests
import json
import random
import string
from random import randint
from data_bulk import *

def test_contact_list():

    url = "http://givvy-api.projestic.com/api/v1/contacts/bulk"
    headers = {"Authorization": "Bearer 3cc828bd49e868908b7d5892c3c38f5e16826ab9a5a724aeabd0cd96977784c7",
               "Content-Type": "application/json", "Accept": "application/json"}
    response = requests.post(url, headers=headers, json=data_bulk())
    assert response.status_code == 201
    print(response.json())

test_contact_list()





