# В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество в ней символов.
value = 0
dlina = 0
with open('HW_file_final.txt', 'r', encoding='utf 8') as f:
    s = f.readlines()
    for i in s:
        value += 1
        i = i[:-1]
        dlina = len(i)
        print(i, '\n', f'Количество символов в данной строке - {dlina}')
print(f'Всего строк в текстовом документе - {value}')
