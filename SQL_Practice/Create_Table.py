# Create a Database Table
from Connect import connect


def create_table(conn, table_name, columns):
    cursor = conn.cursor()
    columns_sql = ", ".join(columns)
    query = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns_sql});'

    cursor.execute(query)

    conn.commit()

    print("Table Created Successfully.")

    cursor.close()

if __name__ == '__main__':
    conn = connect()
    
    if conn:
        create_table(conn, 'user', [
            'id SERIAL PRIMARY KEY',
            'name VARCHAR(100)',
            'email VARCHAR(100)'
        ])
