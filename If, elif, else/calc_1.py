# Калькулятор. Пользователь вводит с клавиатуры числа и операцию и получает результат.
a = float(input('Введите первое число: '))
c = input('Введите одну из следующих операций +, -, /, *: ')
b = float(input('Введите второе число: '))
if c == '+':
    print('Результат суммы ваших чисел', a+b)
elif c == '-':
    print('Результат вычитания ваших чисел', a-b)
elif c == '/':
    print('Результат деления ваших чисел', a/b)
elif c == '*':
    print('Результат произведения ваших чисел', a*b)
else:
    print('Вы ввели неверное значение для операции')