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

    connection.commit()


# for number in range(1, 5):  # добавление продуктов в таблицу
#     cursor.execute(f'''
#     INSERT INTO Products VALUES('{number}', 'Продукт {number}', 'Описание {number}', '{number * 100}')
#     ''')


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products
