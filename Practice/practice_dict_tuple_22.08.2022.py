# 1. Создать произвольный словарь
# 2. Добавить новый элемент с ключом типа str и значением типа int
# 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)
# 4. Получить элемент по ключу
# 5. Удалить элемент по ключу
# 6. Получить список ключей словаря

a = {1:'hello','2':5,'sun':'red'}
a['str_']=19
a[('a','e',4,3,'f')]=[1,2,3,4,5]
print(a['2'])
del a[1]
print(list(a.keys()))
print(a)