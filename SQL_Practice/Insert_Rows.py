# Add Records to the Users Table
import psycopg2

from Connect import connect
from psycopg2 import sql


def insert_rows(conn=None, table_name='', columns=[], row_info=(), return_identifier='id'):
    """
    Insert a new User into the User table and return the User ID.

    :param conn: Object, Database Connection
    :param table_name: String, Database Table Name
    :param columns: List of Column Names
    :param row_info: List of Row Info (Each as Tuples) to Insert, Each Column Value
    :param return_identifier: String, primary key identifier to return
    :returns table_ids: List of ID's of new User Records.
    :rtype: list of int or other return_identifier
    :returns returns_list: List of Return Items E.g. ("{{first_name}} {{last_name}}") Value if users table, else []
    :rtype: list of str
    """
    print(f'************* Now Inserting into the {table_name.upper()} Table *************')
    cursor = conn.cursor()
    columns_sql = ', '.join(['%s'] * len(columns))
    col_identifiers = [sql.Identifier(name) for name in columns]
    cols = sql.SQL(', ').join(col_identifiers)

    if table_name == 'book_authors':
        returning_identifiers = [
            sql.Identifier(columns[0]),
            sql.Identifier(columns[1])
        ]
    elif table_name == 'users':
        returning_identifiers = [
            sql.Identifier(return_identifier),
            sql.Identifier(columns[0]),
            sql.Identifier(columns[1])
        ]
    else:
        returning_identifiers = [
            sql.Identifier(return_identifier)
        ]

    returning = sql.SQL(', ').join(returning_identifiers)

    # The SQL statement uses %s as a placeholder for the Table fields to prevent SQL injection
    # query = """
    #     INSERT INTO {} ({}, {}, {})
    #     VALUES (%s, %s, %s)
    #     RETURNING id, {}, {};
    # """
    query = f"""
        INSERT INTO {{}} ({{}})
        VALUES ({columns_sql})
        RETURNING {{}};
    """
    table_ids = []
    returns_list = []
    successful_inserts = 0
    failed_inserts = 0

    # Execute Many - Wont Continue If One Already Exists with Unique Constraint
    # try:
    #     query = cursor.executemany(
    #         sql.SQL(query).format(
    #             sql.Identifier(table_name),
    #             sql.Identifier(columns[0]),
    #             sql.Identifier(columns[1]),
    #             sql.Identifier(columns[2])
    #         ),
    #         row_info
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

    # for first_name, last_name, email in row_info:
    for row in row_info:
        try:
            # cursor.execute(
            #     sql.SQL(query).format(
            #         sql.Identifier(table_name),
            #         sql.Identifier(columns[0]),
            #         sql.Identifier(columns[1]),
            #         sql.Identifier(columns[2]),
            #         sql.Identifier(columns[0]),
            #         sql.Identifier(columns[1])
            #     ),
            #     row
            # )
            cursor.execute(
                sql.SQL(query).format(
                    sql.Identifier(table_name),
                    cols,
                    returning
                ),
                row
            )
        except (Exception, psycopg2.DatabaseError, psycopg2.IntegrityError) as e:
            print(f'Error Inserting {table_name} Table Record: {e}')
            conn.rollback()
            failed_inserts += 1
        else:
            conn.commit()
            successful_inserts += 1
            executed_query_bytes = cursor.query
            executed_query_str = executed_query_bytes.decode('utf-8')

            print(f'Executed Query: {executed_query_str}')

            result = cursor.fetchall()[0]

            table_ids.append(result[0])

            if table_name == 'book_authors':
                returns_list.append(str(result[0]) + '-' + str(result[1]))
            elif table_name == 'users':
                returns_list.append(result[1] + ' ' + result[2])

    print(f'{successful_inserts} Records Inserted Successfully.')
    print(f'{failed_inserts} Records Failed to Insert')
    print(f'List of "{table_name}" Table ID\'s:', table_ids)

    if table_name == 'book_authors':
        print('List of Book/Author ID\'s:', returns_list)
    elif table_name == 'users':
        print('List of User Names:', returns_list)

    print('--------------------------------------------------')

    # Close the Cursor and Connection
    if cursor:
        cursor.close()

    # if conn:
    #     conn.close()

    return table_ids, returns_list


if __name__ == '__main__':
    conn = connect()

    if conn:
        # Insert Rows
        insert_rows(
            conn, 'users', [
                'first_name',
                'last_name',
                'email'
            ],
            [
                ('Mike', 'Dinder', 'mike@mikedinder.com'),
                ('Robb', 'Dinder', 'robb@mikedinder.com'),
                ('Roger', 'ROlast', 'roger@mikedinder.com'),
                ('Chris', 'CHlast', 'chris@mikedinder.com'),
                ('Sean', 'SElast', 'sean@mikedinder.com'),
                ('Catherine', 'CAlast', 'catherine@mikedinder.com'),
                ('Liz', 'Llast', 'liz@mikedinder.com'),
                ('Ruby', 'RUlast', 'ruby@mikedinder.com'),
                ('Rachel', 'RAlast', 'rachel@mikedinder.com'),
                ('Vienna', 'Vlast', 'vienna@mikedinder.com'),
            ]
        )

        conn.close()
