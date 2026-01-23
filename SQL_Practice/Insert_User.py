# Add Records to the User Table
import psycopg2

from Connect import connect
from psycopg2 import sql


def insert_user(conn, table_name, columns, user_info):
    """
    Insert a new User into the User table and return the User ID.

    :param conn: Database Connection
    :param table_name: Database Table Name
    :param columns: List of Column Names
    :param user_info: List of User Info (Each as Tuples) to Insert, Each Column Value
    :returns user_ids: List of ID's of new User Records.
    :rtype: list of int
    :returns user_names: List of User Names ("{{first_name}} {{last_name}}") Value
    :rtype: list of str
    """
    cursor = conn.cursor()
    # The SQL statement uses %s as a placeholder for the User fields to prevent SQL injection
    query = """
            INSERT INTO {} ({}, {}, {})
            VALUES (%s, %s, %s)
            RETURNING id, {}, {};
        """
    user_ids = []
    user_names = []
    successful_inserts = 0
    failed_inserts = 0

    # try:
    #     Execute Many - Wont Continue If One Already Exists with Unique Constraint
    #     query = cursor.executemany(
    #         sql.SQL(query).format(
    #             sql.Identifier(table_name),
    #             sql.Identifier(columns[0]),
    #             sql.Identifier(columns[1]),
    #             sql.Identifier(columns[2])
    #         ),
    #         user_info
    #     )
    # except (Exception, psycopg2.DatabaseError) as e:
    #     print(f'Error Inserting User Record: {e}')
    #     conn.rollback()
    # else:
    #     conn.commit()
    #     executed_query_bytes = cursor.query
    #     executed_query_str = executed_query_bytes.decode('utf-8')

    #     print(f'Executed Query: {executed_query_str}')
    #     print(f'{cursor.rowcount} Records Inserted Successfully.')

    for first_name, last_name, email in user_info:
        try:
            cursor.execute(
                sql.SQL(query).format(
                    sql.Identifier(table_name),
                    sql.Identifier(columns[0]),
                    sql.Identifier(columns[1]),
                    sql.Identifier(columns[2]),
                    sql.Identifier(columns[0]),
                    sql.Identifier(columns[1])
                ),
                (first_name, last_name, email)
            )
        except (Exception, psycopg2.DatabaseError, psycopg2.IntegrityError) as e:
            print(f'Error Inserting User Record: {e}')
            conn.rollback()
            failed_inserts += 1
        else:
            conn.commit()
            successful_inserts += 1
            executed_query_bytes = cursor.query
            executed_query_str = executed_query_bytes.decode('utf-8')

            print(f'Executed Query: {executed_query_str}')

            result = cursor.fetchall()[0]

            user_ids.append(result[0])
            user_names.append(result[1] + ' ' + result[2])

    print(f'{successful_inserts} Records Inserted Successfully.')
    print(f'{failed_inserts} Records Failed to Insert')
    print('List of User ID\'s:', user_ids)
    print('List of User Names:', user_names)

    # Close the Cursor and Connection
    if cursor:
        cursor.close()

    if conn:
        conn.close()

    return user_ids, user_names


if __name__ == '__main__':
    conn = connect()

    if conn:
        # Insert User
        insert_user(
            conn, 'user', [
                'first_name',
                'last_name',
                'email'
            ],
            [
                ('Mike', 'Dinder', 'mike@mikedinder.com'),
                ('Robb', 'Dinder', 'robb@mikedinder.com'),
                # ('Roger', 'ROlast', 'roger@mikedinder.com'),
                # ('Chris', 'CHlast', 'chris@mikedinder.com'),
                # ('Sean', 'SElast', 'sean@mikedinder.com'),
                # ('Catherine', 'CAlast', 'catherine@mikedinder.com'),
                # ('Liz', 'Llast', 'liz@mikedinder.com'),
                # ('Ruby', 'RUlast', 'ruby@mikedinder.com'),
                # ('Rachel', 'RAlast', 'rachel@mikedinder.com'),
                # ('Vienna', 'Vlast', 'vienna@mikedinder.com'),
            ]
        )
