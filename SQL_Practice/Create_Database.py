# Generic Create a PostgreSQL Database
import os
import psycopg2

from dotenv import load_dotenv
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Load Environment Variables
load_dotenv()

# Database connection parameters (connect to a default database first, e.g., 'postgres')
DB_NAME_TO_CREATE = 'fiddle_database'
CONN_PARAMS = {
    'user': os.getenv('DB_USER'),            # Default/Master User
    'password': os.getenv('DB_PASSWORD'),    # Actual Work Environment - Make this a Secret Variable
    'host': os.getenv('DB_HOST'),            # Default localhost
    'port': os.getenv('DB_PORT')             # Default Port: 5432
}
conn = None
cursor = None

try:
    # Connect to the default 'postgres' database
    conn = psycopg2.connect(dbname='postgres', **CONN_PARAMS)

    # Set the connection to autocommit mode
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Create a cursor object
    cursor = conn.cursor()

    # Use the psycopg2.sql module to safely format the query
    # This helps prevent SQL injection
    create_db_query = sql.SQL('CREATE DATABASE {}').format(
        sql.Identifier(DB_NAME_TO_CREATE)
    )

    # Execute the query to create the new database
    cursor.execute(create_db_query)
    print(f'Database "{DB_NAME_TO_CREATE}" created successfully!')

except psycopg2.Error as e:
    print(f'An error occurred: {e}')

    # Check if Database Already Exists - Usually if running this script two times in a row.
    if 'already exists' in str(e):
        print(f'The Database "{DB_NAME_TO_CREATE}" Already Exists! No Database Created...')

finally:
    # Close the Cursor and Connection
    if cursor:
        cursor.close()

    if conn:
        conn.close()
