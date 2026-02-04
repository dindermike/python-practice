# Running basic DELETE Requests using a web platform called ReqRes (https://reqres.in/) to mock API Endpoints
# For me to hit via Python requests below.
import os
import requests
import sys

from GET import get_books
from dotenv import load_dotenv


# Load Environment Variables
load_dotenv()


def delete_book(id=None, info_print=True) -> None:
    """
    Takes in a ReqRes record ID and performs a full update of that record (PUT). Returns updated record.

    :param id: Int or String, number ID of the book to lookup and return the actual ID in ReqRes.
    :param info_print: Boolean, Optional turn off print statements.
    :returns: None
    :rtype: None
    """

    if os.getenv('REQRES_TOKEN') is None or os.getenv('REQRES_TOKEN') == os.getenv('REQRES_DUMMY_VALUE'):
        print('You Need A Validated Token to Continue!')
        sys.exit()
    else:
        book_id = get_books(id, False, False)

        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {os.getenv("REQRES_TOKEN")}',
            'Connection': 'keep-alive',
            'x-api-key': os.getenv('X_API_PROD_KEY')
        }

        response = requests.delete(
            os.getenv('REQRES_BASE_URL') + os.getenv('REQRES_COLLECTION_BOOKS') + '/' + book_id,
            headers=headers
        )

        # Get Status Code
        status = response.status_code

        if status == 204:
            if info_print:
                print('Success! Book Deleted')
        else:
            if info_print:
                print('There Was A Problem Deleting Your Book!')

                # Get JSON Response
                result = response.json()

                if 'message' in result:
                    print(result['message'])

        return None


if __name__ == '__main__':
    delete_book(101)
