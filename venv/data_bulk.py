import random
import string
from random import randint

def random_with_N_digits(n):
 range_start = 10 ** (n - 1)
 range_end = (10 ** n) - 1
 return randint(range_start, range_end)


def random_char(y):
 return ''.join(random.choice(string.ascii_letters) for x in range(y))


def data_bulk():
    phone = '+38{}'.format(random_with_N_digits(7))
    newEmail = random_char(7) + "@gmail.com"
    phone_2 = '+38{}'.format(random_with_N_digits(7))
    newEmail_2 = random_char(7) + "@gmail.com"
    body = [
   {
    "first_name": "fwef",
    "last_name": "ewf",
    "email": newEmail,
    "mobile_phone": phone,
    "middle_name": "asf",
    "nickname": "ewfunt",
    "relationship_status": "nus",
    "title": "iwefj",
    "suffix": "omn",
    "contact_method": "email",
    "birthdate": 855698400000,
    "gender": "unspecified"
   },
   {
    "first_name": "fwsdfef",
    "last_name": "eweff",
    "email": newEmail_2,
    "mobile_phone": phone_2,
    "middle_name": "asff",
    "nickname": "ewfeunt",
    "relationship_status": "nusf",
    "title": "iweefj",
    "suffix": "ofmn",
    "contact_method": "email",
    "birthdate": 85569840300,
    "gender": "unspecified"
  }
]
    return body