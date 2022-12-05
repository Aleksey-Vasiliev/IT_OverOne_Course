import sqlite3

spis = ['world', 1, 4, 'England', 6]

# Создаём Базу данных
twoTable = sqlite3.connect('twoTable.db')
# Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
cursor = twoTable.cursor()
# Создадим первую таблицу с колонкой для текстовых данных
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT) ''')
# Создадим вторую таблицу с колонкой для числовых данных
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER) ''')

for i in spis:
    if type(i) is str:
        cursor.execute(""" INSERT into tab_1(col_1) VALUES(?)""", (i,))
        dlina = len(i)
        cursor.execute(""" INSERT into tab_2(col_1) VALUES(?)""", (dlina,))
        twoTable.commit()
    elif type(i) is int or float:
        if i % 2 == 0:
            cursor.execute(""" INSERT into tab_2(col_1) VALUES(?)""", (i,))
        else:
            cursor.execute(""" INSERT into tab_1(col_1) VALUES('нечётное')""")
        twoTable.commit()
cursor.execute('''SELECT*FROM tab_1''')
j = cursor.fetchall()
print(j)
cursor.execute('''SELECT*FROM tab_2''')
k = cursor.fetchall()
print(k)
print('Выведен результат до изменения таблиц.' '\n')
if len(k) > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
    twoTable.commit()
else:
    cursor.execute('''UPDATE tab_1 SET col_1 = 'hello' WHERE id = 1''')
    twoTable.commit()
cursor.execute('''SELECT*FROM tab_1''')
j = cursor.fetchall()
print(j)
cursor.execute('''SELECT*FROM tab_2''')
k = cursor.fetchall()
print(k)
print('Выведен результат после изменения таблиц.')

