# General Connection Function (Default Practice Database)
import os
import psycopg2

from dotenv import load_dotenv
from psycopg2 import OperationalError
from typing import Union


# Load Environment Variables
load_dotenv()


def connect() -> Union[object, None]:
    """
    Connect to the PostgreSQL database server

    :returns: Connection object or None
    :rtype: Object or None
    """
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        print('Connection Successful!')
        return conn
    except OperationalError as e:
        print(f'Error Connecting to the Database: {e}')
        return None


if __name__ == '__main__':
    print('Practice Connecting...')
    connection = connect()

    if connection:
        print('Connected...')
        connection.close()
        print('Connection Closed!')
