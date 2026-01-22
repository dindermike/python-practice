# Add Records to the User Table
import psycopg2

from Connect import connect
from psycopg2 import sql
from psycopg2.extensions import AsIs


def insert_user(conn, table_name, columns, user_info):
    """
    Insert a new User into the User table and return the User ID.
    
    :param conn: Database Connection
    :param table_name: Database Table Name
    :param columns: List of Column Names
    :param user_info: List of Users, Each Column Value
    :returns user_id: ID of new User Record.
    :rtype: int
    :returns user_name: User Name Value
    :rtype: str
    """
    cursor = conn.cursor()
    # The SQL statement uses %s as a placeholder for the User fields to prevent SQL injection
    query = """
            INSERT INTO %s (%s, %s, %s)
            VALUES (%s, %s, %s);
        """
    user_id = None
    user_name = None

    try:
        cursor.execute(
            query,
            [
                table_name,
                columns[0],
                columns[1],
                columns[2],
                user_info[0],
                user_info[1],
                user_info[2]
            ]
        )
    except (Exception, psycopg2.DatabaseError) as e:
        print(f"Error Inserting User Record: {e}")
        conn.rollback()
    else:
        conn.commit()
        results = cursor.fetchall()

        for row in results:
            print(row)
            user_name = ''
        
        conn.close()

    return user_id, user_name

if __name__ == '__main__':
    conn = connect()

    if conn:
        # Insert User
        insert_user(conn, 'user', [
            'first_name',
            'last_name',
            'email'
        ], [
            'Mike',
            'Dinder',
            'dindermike@hotmail.com'
        ])