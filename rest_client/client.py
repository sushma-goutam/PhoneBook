import requests


# This will help in case we need to change url later
URL = "http://127.0.0.1:8000"

def get_token():
    # Get auth token
    url = f"{URL}/api/auth/"
    response = requests.post(url,
                             data={'username': 'admin',
                                   'password': 'admin'}
                             )
    print(response.text)
    # return response.text
    return response.json()


def get_contact():
    url = f"{URL}/api/contact_list/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.get(url, headers=header)

    contacts = response.json()
    for c in contacts:
        print(c)


def create_contact(count):
    url = f"{URL}/api/contact_list/"
    data = {
        "id": count,
        "first_name": "Mayank",
        "last_name": "Nayak",
        "phone_number": "234567"
    }
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.post(url, data=data, headers=header)
    print(response.text)


def create_many_contacts(count):
    """ This is useful in feeding data from excel to django db """
    for i in range(1, count + 1):
        create_contact(i)


create_contact()
