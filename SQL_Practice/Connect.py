# General Connection Function (Default Practice Database)
import os
import psycopg2

from dotenv import load_dotenv
from psycopg2 import OperationalError

# Load Environment Variables
load_dotenv()

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print("Connection successful.")
        return conn
    except OperationalError as e:
        print(f"Error connecting to the database: {e}")
        return None

if __name__ == '__main__':
    connection = connect()
    if connection:
        print('Connected')
        connection.close()
        print("Connection closed.")