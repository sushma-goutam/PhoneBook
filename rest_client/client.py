import requests


def get_token():
    # Get auth token
    url = "http://127.0.0.1:8000/api/auth/"
    response = requests.post(url,
                             data={'username': 'admin',
                                   'password': 'admin'}
                             )
    print(response.text)
    # return response.text
    return response.json()


def get_data():
    # Get auth token
    url = "http://127.0.0.1:8000/api/contact_list/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.get(url, headers=header)

    contacts = response.json()
    for c in contacts:
        print(c)


get_data()
