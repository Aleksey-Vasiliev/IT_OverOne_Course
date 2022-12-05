# Пользователь вводит десятизначное число.
# Программа находит в веденном числе все четные цифры и выводит их на экран.
user_number = input('Введите десятизначное число: ')
ost = 0
res = ''
user_number = int(user_number)
if user_number > 999999999 and user_number < 10000000000:
    user_number = str(user_number)
    for i in user_number:
        i = int(i)
        ost = i % 2
        if ost == 0 and i != 0:
            ost = str(i)
            res = res + ost
    else:
        print('Четные цифры в Вашем числе:')
        for i in res:
            print(i)
else:
    print('Вы ввели не десятизначное число')