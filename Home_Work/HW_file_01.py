# Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел.
# Вывести в файл ‘output.txt’ их разность
a_schet = 0
b_schet = 0
with open('input.txt', 'w') as f:
    f.write(input('Введите первое число: '))
    f.write(' ')
    f.write(input('Введите второе число: '))
with open('input.txt', 'r') as f:
    line = (f.read())
    line_schet = len(line)
    for i in line:
        if i != ' ':
            a_schet += 1
        else:
            break
    b_schet = line_schet - (a_schet + 1)
    a = line[0:a_schet]
    line_schet += 1
    b = line[a_schet:line_schet]
with open('output.txt', 'w', encoding='utf-8') as k:
    res = int(a)-int(b)
    k.write(f'Разность между первым и вторым введнными числами составляет: {res}')
