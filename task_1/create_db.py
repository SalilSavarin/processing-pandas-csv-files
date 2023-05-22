import sqlite3


def create_db():
    conn = sqlite3.connect('library.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS book
                        (id_book INTEGER PRIMARY KEY,
                        title TEXT,
                        author TEXT,
                        publisher TEXT,
                        year_of_publishing INTEGER,
                        city_of_publishing TEXT,
                        number_of_pages INTEGER,
                        id_copy INTEGER)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS book_lending
                        (id INTEGER PRIMARY KEY,
                        id_copy INTEGER,
                        data_lend DATE,
                        date_return DATE,
                        library_card_number INTEGER,
                        FOREIGN KEY (id_copy) REFERENCES book (id_book))''')
    conn.execute('''CREATE TABLE IF NOT EXISTS reader
                        (id INTEGER PRIMARY KEY,
                        library_card_number INTEGER,
                        last_name TEXT,
                        name TEXT,
                        surname TEXT,
                        date_of_birth DATE,
                        gender TEXT,
                        address TEXT,
                        phone TEXT,
                        FOREIGN KEY (library_card_number) REFERENCES book_lending (library_card_number))''')
    conn.commit()
    conn.close()


create_db()
