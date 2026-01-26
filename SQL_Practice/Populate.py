# Populate database using existing functions to create other tables/records that are not associated with those specific
# practice files.
import datetime

from Connect import connect
from Create_Table import create_table
from Insert_Rows import insert_rows
from psycopg2.extensions import AsIs


if __name__ == '__main__':
    conn = connect()

    if conn:
        create_table(conn, 'authors', [
            AsIs('author_id SERIAL PRIMARY KEY'),
            AsIs('first_name VARCHAR(100) NOT NULL'),
            AsIs('last_name VARCHAR(100) NOT NULL'),
            AsIs('biography TEXT'),
            AsIs('birth_date DATE'),
            AsIs('created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP'),
            AsIs('UNIQUE(first_name, last_name)')
        ])

        create_table(conn, 'publishers', [
            AsIs('publisher_id SERIAL PRIMARY KEY'),
            AsIs('name VARCHAR(200) NOT NULL'),
            AsIs('address TEXT'),
            AsIs('city VARCHAR(100)'),
            AsIs('state VARCHAR(50)'),
            AsIs('zip_code VARCHAR(10)'),
            AsIs('phone VARCHAR(20)'),
            AsIs('email VARCHAR(200)'),
            AsIs('created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP'),
            AsIs('UNIQUE(name)'),
            AsIs('UNIQUE(email)')
        ])

        create_table(conn, 'books', [
            AsIs('book_id SERIAL PRIMARY KEY'),
            AsIs('title VARCHAR(300) NOT NULL'),
            AsIs('isbn VARCHAR(13) UNIQUE NOT NULL'),
            AsIs('publisher_id INTEGER REFERENCES publishers(publisher_id)'),
            AsIs('publication_date DATE'),
            AsIs('price DECIMAL(10, 2) NOT NULL'),
            AsIs('stock_quantity INTEGER DEFAULT 0'),
            AsIs('description TEXT'),
            AsIs('genre VARCHAR(50)'),
            AsIs('created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP')
        ])

        create_table(conn, 'book_authors', [
            AsIs('book_id INTEGER REFERENCES books(book_id) ON DELETE CASCADE'),
            AsIs('author_id INTEGER REFERENCES authors(author_id) ON DELETE CASCADE'),
            AsIs('PRIMARY KEY (book_id, author_id)')
        ])

        create_table(conn, 'customers', [
            AsIs('customer_id SERIAL PRIMARY KEY'),
            AsIs('first_name VARCHAR(100) NOT NULL'),
            AsIs('last_name VARCHAR(100) NOT NULL'),
            AsIs('email VARCHAR(100) UNIQUE NOT NULL'),
            AsIs('phone VARCHAR(20)'),
            AsIs('address TEXT'),
            AsIs('city VARCHAR(100)'),
            AsIs('state VARCHAR(50)'),
            AsIs('zip_code VARCHAR(10)'),
            AsIs('created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP'),
            AsIs('UNIQUE(first_name, last_name)')
        ])

        create_table(conn, 'orders', [
            AsIs('order_id SERIAL PRIMARY KEY'),
            AsIs('customer_id INTEGER REFERENCES customers(customer_id)'),
            AsIs('order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP'),
            AsIs('total_amount DECIMAL(10, 2) NOT NULL'),
            AsIs('status VARCHAR(20) DEFAULT \'pending\''),
            AsIs('shipping_address TEXT'),
            AsIs('city VARCHAR(100)'),
            AsIs('state VARCHAR(50)'),
            AsIs('zip_code VARCHAR(10)'),
            AsIs('payment_method VARCHAR(50)')
        ])

        create_table(conn, 'order_items', [
            AsIs('order_item_id SERIAL PRIMARY KEY'),
            AsIs('order_id INTEGER REFERENCES orders(order_id) ON DELETE CASCADE'),
            AsIs('book_id INTEGER REFERENCES books(book_id)'),
            AsIs('quantity INTEGER NOT NULL'),
            AsIs('unit_price DECIMAL(10, 2) NOT NULL'),
            AsIs('subtotal DECIMAL(10, 2) NOT NULL')
        ])

        # Insert Rows
        insert_rows(
            conn, 'authors', [
                'author_id',
                'first_name',
                'last_name',
                'biography',
                'birth_date'
            ],
            [
                ('10000', 'Mike', 'Dinder', 'Information Technology Author of a Django Book', datetime.date(1985, 12, 15)),
                ('10001', 'Michael', 'Binder', 'Writer of fiction books, mostly Sci-fi and Fantasy', datetime.date(1987, 9, 13)),
                ('10002', 'Robb', 'Dinder', 'Writer of awesome baking books', datetime.date(1989, 4, 20)),
                ('10003', 'Roger', 'ROLast', 'Master debator of anything that is considered a "hot topic"', datetime.date(1999, 4, 19)),
                ('10004', 'Rachel', 'RALast', 'Specializes in spy tactics, specifically how to transition from job to job and make people believe you are an expert in that field, even when you are not.', datetime.date(2001, 7, 12)),
                ('10005', 'Ruby', 'RULast', 'Specializes in adaptability through difficult situations.', datetime.date(2000, 2, 14)),
                ('10006', 'Liz', 'LILast', 'Publishes stories of how to become a pilot as well as specializes in how to be sassy to people who need it.', datetime.date(2005, 6, 25)),
            ]
        )

        conn.close()