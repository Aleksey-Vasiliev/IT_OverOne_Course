import sqlite3

# .connect как бы устанавливает соединение с БД, в скобках указано название, но также можно пропистаь путь,
# где необходимо создать БД.
with sqlite3.connect('hw_sqlite.db') as book_db:
    cursor = book_db.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS book(book_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(50),
            author VARCHAR(30), price DECIMAL(8, 2), amount INT) """)
    cursor.execute(""" INSERT into book(title, author, price, amount) VALUES('Жизнь таксиста', 'Эдвард Хома', 8, 3)""")
    cursor.execute(""" INSERT into book(title, author, price, amount) VALUES('Хороший продажник', 'Эдвард Хома', 9, 2)""")
    book_db.commit()
    cursor.execute('''SELECT*FROM book''')
    k = cursor.fetchall()
    print(k)