# Create a Database Table
import psycopg2

from Connect import connect
from psycopg2 import sql
from psycopg2.extensions import AsIs


def create_table(conn, table_name='', columns=None):
    """
    Insert a new User into the User table and return the User ID.

    :param conn: Database Connection
    :param table_name: Database Table Name
    :param columns: List, Specifies the columns to write
    :returns: Nothing - Prints Status as Prompt Dialogue
    """
    cursor = conn.cursor()
    columns_sql = ', '.join(['%s'] * len(columns))
    query = f'CREATE TABLE IF NOT EXISTS {{}} ({columns_sql});'

    try:
        cursor.execute(
            sql.SQL(query).format(
                sql.Identifier(table_name)
            ),
            columns
        )
    except (Exception, psycopg2.DatabaseError) as e:
        print(f"Error Creating Table: {e}")
        conn.rollback()
    else:
        conn.commit()
        executed_query_bytes = cursor.query
        executed_query_str = executed_query_bytes.decode('utf-8')

        print(f"Executed Query: {executed_query_str}")
        print("Table Created Successfully.")
    finally:
        # Close the Cursor and Connection
        if cursor:
            cursor.close()

        if conn:
            conn.close()


if __name__ == '__main__':
    conn = connect()

    if conn:
        create_table(conn, 'user', [
            AsIs('id SERIAL PRIMARY KEY'),
            AsIs('first_name VARCHAR(100)'),
            AsIs('last_name VARCHAR(100)'),
            AsIs('email VARCHAR(200)')
        ])
