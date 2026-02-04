# Running basic PATCH Requests using a web platform called ReqRes (https://reqres.in/) to mock API Endpoints
# For me to hit via Python requests below.
# NOTE: ReqRes does not currently support PATCH Request for partial update or at least not for my free plan. If they did
# it would look like the example below.
import json
import os
import requests
import sys

from GET import get_books
from dotenv import load_dotenv
from typing import Union


# Load Environment Variables
load_dotenv()


def partial_update_book(id=None, info_print=True) -> Union[dict, None]:
    """
    Takes in a ReqRes record ID and performs a partial update of that record (PATCH). Returns updated record.

    :param id: Int or String, number ID of the book to lookup and return the actual ID in ReqRes.
    :param info_print: Boolean, Optional turn off print statements.
    :returns: Actual Book ID found in ReqRes Database or dictionary of books
    :rtype: dict or None
    """

    if os.getenv('REQRES_TOKEN') is None or os.getenv('REQRES_TOKEN') == os.getenv('REQRES_DUMMY_VALUE'):
        print('You Need A Validated Token to Continue!')
        sys.exit()
    else:
        book_id = get_books(id, False, False)

        payload = {
            'data': {
                'genre': 'New Genre'
            }
        }
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {os.getenv("REQRES_TOKEN")}',
            'Connection': 'keep-alive',
            'x-api-key': os.getenv('X_API_PROD_KEY')
        }

        response = requests.patch(
            os.getenv('REQRES_BASE_URL') + os.getenv('REQRES_COLLECTION_BOOKS') + '/' + book_id,
            json=payload,
            headers=headers
        )

        # Get JSON Response
        result = response.json()

        # Get Status Code
        status = response.status_code

        if status == 200:
            if info_print:
                print('Success! Book Updated')

            if 'data' in result:
                data = result['data']

                if info_print:
                    json_formatted_str = json.dumps(data, indent=2)
                    print(json_formatted_str)

                record = data['data']

                if info_print:
                    print('--------------------------------------------------')
                    print('Updated Record...')
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
    partial_update_book(101)
