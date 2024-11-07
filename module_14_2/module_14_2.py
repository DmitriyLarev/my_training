import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# age = 0
# for i in range(1, 11): #  добавление данных в таблицу
#     age += 10
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i}', f'example{i}@gmail.com', age, 1000))

# for i in range(1, 11, 2): #  обновление данных в таблице
#     cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i))

# for i in range(1, 11, 3): #  удаление данных
#     cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

# cursor.execute('SELECT * FROM Users WHERE age != 60')
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

# cursor.execute('DELETE FROM Users WHERE id == 6') #  удаление пользователя с id 6

cursor.execute('SELECT COUNT(*) FROM Users')  # подсчет количества пользователей
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')  # подсчет суммы балансов пользователей
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)
connection.commit()
connection.close()
