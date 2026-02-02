# Running basic GET Requests using a web platform called ReqRes (https://reqres.in/) to mock API Endpoints
# For me to hit via Python requests below.
import json
import os
import requests
import sys

from dotenv import load_dotenv


# Load Environment Variables
load_dotenv()


if os.getenv('REQRES_TOKEN') is None or os.getenv('REQRES_TOKEN') == os.getenv('REQRES_DUMMY_VALUE'):
    print('You Need A Validated Token to Continue!')
    sys.exit()
else:
    token = None

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {os.getenv('REQRES_TOKEN')}',
        'Connection': 'keep-alive',
        'x-api-key': os.getenv('X_API_PROD_KEY')
    }

    response = requests.get(os.getenv('REQRES_BASE_URL') + os.getenv('REQRES_COLLECTION_BOOKS'), headers=headers)

    # Get JSON Response
    result = response.json()

    # Get Status Code
    status = response.status_code

    if status == 200:
        print('Success! Books Retreived')

        if 'meta' in result:
            meta = result['meta']
            print('Page:', meta['page'])
            print('Limit:', meta['limit'])
            print('Total:', meta['total'])
            print('Pages:', meta['pages'])

        if 'data' in result:
            data = result['data']
            json_formatted_str = json.dumps(data, indent=2)
            print(json_formatted_str)

            for book in data:
                record = book['data']

                if record['title'] == 'Becoming an Enterprise Django Developer':
                    print('--------------------------------------------------')
                    print('Example Record Found...')
                    print(record['title'])
                    print(record['price'])
                    print(record['genre'])
                    print(record['description'])
                    print(record['book_id'])
                    print(record['website'])
                    print(record['publisher_id'])
                    print(record['stock_quantity'])
                    print(record['publication_date'])
                    print('--------------------------------------------------')
        else:
            if 'message' in result:
                print(result['message'])
    else:
        if 'message' in result:
            print(result['message'])
