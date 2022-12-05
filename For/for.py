# Пользователь вводит трехзначное число. Программа суммирует цифры введенного числа и выводит на экран.
user_number = input('Введите трехзначное число: ')
res = 0
user_number = int(user_number)
if user_number > 100 and user_number < 1000:
    user_number = str(user_number)
    for i in user_number:
        i = int(i)
        res = res + i
    else:
        print('Результат сложения цифр Вашего числа:', res)
else:
    print('Вы ввели не трехзначное число')