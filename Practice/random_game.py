import random

random_number = random.randint(1, 5)
user_number = input('Угадай число (от 1 до 5): ')

if user_number == random_number:
    print("Вы угадали!")

else:
    print('Вы не угадали :c')
    print(f'Было загадоно число {random_number}')