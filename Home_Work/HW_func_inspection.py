# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – количество букв.
# Сделать проверку со всеми этими случаями.


vvod = 'afga23432321sdfag234'


def len_word(a):
    summa = 0
    for i in a:
        if type(i) == str:
            summa += len(i)
        else:
            continue
    return summa


def spis(a):
    summa_letters = 0
    summa_numbers = 0
    for i in a:
        if type(i) == str:
            summa_letters += len(i)
        elif type(i) == int or float:
            summa_numbers += i
        else:
            continue
    return summa_numbers, summa_letters


def ne_chet(a):
    summa = 0
    if type(a) == int:
        a = str(a)
        for i in a:
            i = int(i)
            if i % 2 != 0:
                summa += 1
            else:
                continue
    return summa

if type(vvod) == tuple:
    print(f'Длина всех слов в кортеже: {len_word(vvod)}')
elif type(vvod) == str:
    print(f'Длина строки: {len(vvod)}')
elif type(vvod) == list:
    print(f'Кол-во букв в списке: {spis(vvod)[1]}, а сумма всех чисел в списке: {spis(vvod)[0]}')
elif type(vvod) == int or float:
    print(f'Кол-во нечетных цифр в числе {ne_chet(vvod)}')
