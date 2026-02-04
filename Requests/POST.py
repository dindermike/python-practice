# Running basic POST Requests using a web platform called ReqRes (https://reqres.in/) to mock API Endpoints
# For me to hit via Python requests below.
import json
import os
import requests
import sys

from datetime import datetime
from dotenv import load_dotenv
from typing import Union
from zoneinfo import ZoneInfo


# Load Environment Variables
load_dotenv()


def create_book(payload={}, info_print=True) -> Union[dict, None]:
    """
    Takes in a payload and creates a new Book record in ReqRes.

    :param payload: Dict, Payload to create.
    :param info_print: Boolean, Optional turn off print statements.
    :returns: Record of book created or None
    :rtype: dict or None
    """

    if os.getenv('REQRES_TOKEN') is None or os.getenv('REQRES_TOKEN') == os.getenv('REQRES_DUMMY_VALUE'):
        print('You Need A Validated Token to Continue!')
        sys.exit()
    else:
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {os.getenv("REQRES_TOKEN")}',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'x-api-key': os.getenv('X_API_PROD_KEY')
        }

        response = requests.post(
            os.getenv('REQRES_BASE_URL') + os.getenv('REQRES_COLLECTION_BOOKS'),
            json=payload,
            headers=headers
        )

        # Get JSON Response
        result = response.json()

        # Get Status Code
        status = response.status_code

        if status == 201:
            if info_print:
                print('Success! Book Created')

            if 'data' in result:
                data = result['data']

                if info_print:
                    json_formatted_str = json.dumps(data, indent=2)
                    print(json_formatted_str)

                record = data['data']

                if info_print and record['title'] == 'King Arthur Baking Company\'s Big Book of Bread':
                    print('--------------------------------------------------')
                    print('Record Created, Details...')
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

                return record
            else:
                if info_print and 'message' in result:
                    print(result['message'])
        else:
            if info_print and 'message' in result:
                print(result['message'])

        return None


if __name__ == '__main__':
    tz = ZoneInfo('America/Phoenix')

    create_book(
        {
            'data': {
                'isbn': '978-1668009741',
                'genre': 'Cooking',
                'price': '29.87',
                'title': 'King Arthur Baking Company\'s Big Book of Bread',
                'book_id': 101,
                'website': 'https://shop.kingarthurbaking.com/items/king-arthur-baking-companys-big-book-of-bread',
                'created_at': datetime(2026, 2, 2, 13, 40, 0, tzinfo=tz).strftime(os.getenv('STD_DATETIME_FMT')),
                'description': 'Master the art of bread baking with 125+ bread recipes for every baker\'s journey.',
                'publisher_id': 20001,
                'stock_quantity': 25,
                'publication_date': datetime(2024, 10, 22, 6, 0, 0, tzinfo=tz).strftime(os.getenv('STD_DATETIME_FMT'))
            }
        }
    )
