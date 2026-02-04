# Running basic GET Requests using a web platform called ReqRes (https://reqres.in/) to mock API Endpoints
# For me to hit via Python requests below.
import json
import os
import requests
import sys

from dotenv import load_dotenv
from typing import Union


# Load Environment Variables
load_dotenv()


def get_books(book_id=None, rwr=False, info_print=True) -> Union[str, dict, None]:
    """
    Get a dict of books or if using book_id parameter return the string ID of that record.

    :param book_id: Int, number ID of the book to lookup and return the actual ID in ReqRes.
    :param rwr: Boolean, Return Whole Record (rwr) True/False, if True return whole data dict.
    :param info_print: Boolean, Optional turn off print statements.
    :returns: Actual Book ID found in ReqRes Database or dictionary of books
    :rtype: str, dict or None
    """

    if os.getenv('REQRES_TOKEN') is None or os.getenv('REQRES_TOKEN') == os.getenv('REQRES_DUMMY_VALUE'):
        print('You Need A Validated Token to Continue!')
        sys.exit()
    else:
        return_id = None
        lookup_title = None
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
            if info_print:
                print('Success! Books Retreived')

            if 'meta' in result and info_print:
                meta = result['meta']
                print('Page:', meta['page'])
                print('Limit:', meta['limit'])
                print('Total:', meta['total'])
                print('Pages:', meta['pages'])

            if 'data' in result:
                data = result['data']

                if info_print:
                    json_formatted_str = json.dumps(data, indent=2)
                    print(json_formatted_str)

                if not book_id:
                    lookup_title = 'Becoming an Enterprise Django Developer'

                for book in data:
                    record = book['data']

                    if book_id:
                        try:
                            book_id = int(book_id)
                        except (ValueError, TypeError):
                            if info_print:
                                print(
                                    f'The "book_id" Variable "{book_id}" is NOT a Number and cannot be converted to '
                                    'one!'
                                )
                        else:
                            if record['book_id'] == book_id:
                                return_id = book['id']
                                lookup_title = record['title']

                    if lookup_title and record['title'] == lookup_title and info_print:
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

                if return_id:
                    return return_id
                else:
                    return data
            else:
                if 'message' in result and info_print:
                    print(result['message'])
        else:
            if 'message' in result and info_print:
                print(result['message'])

        return None


if __name__ == '__main__':
    # book_id = ''
    # get_books()
    # book_id = get_books(101)
    # book_id = get_books('101')
    # print('Book ID:', book_id)

    books = get_books()
    print('Books:', books)
