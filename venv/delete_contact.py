from selenium import webdriver
import requests
import json

def delete_contact():

    url = "http://givvy-api.projestic.com/api/v1/contacts/848"
    headers = {"Authorization": "Bearer 3cc828bd49e868908b7d5892c3c38f5e16826ab9a5a724aeabd0cd96977784c7",
               "Content-Type": "application/json", "Accept": "application/json"}
    create_contact_response = requests.delete(url, headers=headers)
    print(create_contact_response)
    assert create_contact_response.status_code == 200

delete_contact()


