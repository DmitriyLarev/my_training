import sqlite3

connection = sqlite3.connect('telegram.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    );
    ''')

    connection.commit()


def add_user(username, email, age):
    cursor.execute('''
    INSERT INTO Users ('username', 'email', age, 'balance') VALUES (?, ?, ?, ?)
    ''', (username, email, age, 1000))
    connection.commit()


def is_included(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,)).fetchone()
    if check_user is None:
        return False
    else:
        return True


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products
