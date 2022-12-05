# Пользователь вводит два числа с клавиатуры, необходимо вывести на экран все отрицательные числа,
# лежащие между ними. Например, пользователь ввел -5 и 3, на экране вывелось -4,-3,-2,-1 (решить через while).

user_number_1 = int(input('Введите первое число: '))
user_number_2 = int(input('Введите второе число: '))
if user_number_1 < user_number_2:
    while user_number_1 < user_number_2-1 and user_number_1 < 0:
        if user_number_1 == -1 or user_number_1 == user_number_2:
            break
        else:
            user_number_1 = user_number_1 + 1
            print(user_number_1)

else:
    while user_number_2 < user_number_1-1 and user_number_2 < 0:
        if user_number_2 == -1 or user_number_2 == user_number_1:
            break
        else:
            user_number_2 = user_number_2 + 1
            print(user_number_2)

