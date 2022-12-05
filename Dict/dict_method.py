a = {'1': [1,2,3], 2:'hello'}
c_1 = {1, 2, 3, 4, 5}
c_2 = {'hello', 'world', '321', 'sun', 'winter'}
# for key, value in a.items():
#     print(f'Ключ: {key}, значение: {value[2]}')

# for i in a:
#     print(i)

# print(a.items())
# print(a.values())
# print(a.keys())
# print(a.clear())
# b = a.copy()
# print(id(a), id(b))
# print(b)
# a.pop(2)
# print(a)
# print(len(a))
# del a['1']
# print(a)
# if 2 in a:
#     print('yes')
print(dict(zip(c_1, c_2)))