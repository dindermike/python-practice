# Establishes a validated Session with the web platform called ReqRes (https://reqres.in/) to mock API Endpoints
# For me to hit via Python requests in the corresponding files. Their system works by sending a token via email and will
# Require a partial manual process to copy and paste that token.
import os
import requests
import time

from dotenv import load_dotenv, set_key


# Load Environment Variables
load_dotenv()


login = '/api/app-users/login'
verify = '/api/app-users/verify'
token = None

payload = {
    'email': os.getenv('REQRES_USER_EMAIL'),
    'project_id': os.getenv('REQRES_PROJ_ID_1')
}
headers = {
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'x-api-key': os.getenv('X_API_PROD_KEY')
}

response = requests.post(os.getenv('REQRES_BASE_URL') + login, json=payload, headers=headers)

# Get JSON Response
result = response.json()

# Get Status Code
status = response.status_code

if status == 200:
    print('Success!')

    if 'data' in result:
        data = result['data']

        if 'message' in data:
            print(data['message'])

            token = input('Enter the Token Emailed to you: ')
    else:
        if 'message' in result:
            print(result['message'])
else:
    if 'message' in result:
        print(result['message'])

if token:
    print('Validating Token Now...')

    payload = {
        'email': os.getenv('REQRES_USER_EMAIL'),
        'token': token
    }
    headers = {
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'x-api-key': os.getenv('X_API_PROD_KEY')
    }

    response = requests.post(os.getenv('REQRES_BASE_URL') + verify, json=payload, headers=headers)

    # Get JSON Response
    result = response.json()

    # Get Status Code
    status = response.status_code

    if status == 200:
        print('Success! You Are Now Validated!')

        if 'data' in result:
            data = result['data']

            if 'session_token' in data:
                session_token = data['session_token']
                set_key('.env', 'REQRES_TOKEN', session_token)
                print(f'We Have Updated REQRES_TOKEN in the .env File To: {session_token}')
                print('Your Token Will Expire in 1 Hour')

                time.sleep(3600)

                set_key('.env', 'REQRES_TOKEN', os.getenv('REQRES_DUMMY_VALUE'))

            if 'note' in data:
                print('Note:', data['note'])
        else:
            if 'message' in result:
                print(result['message'])
    else:
        if 'message' in result:
            print(result['message'])
