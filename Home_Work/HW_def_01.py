# Создайте функцию, которая принимает на вход неограниченное количество позиционных и именованных аргументов.
# В качестве результата функция должна возвращать только позиционные аргументы с нечетными индексами и ключевые,
# значения которых являются строками.

def homeW(*args, **kwargs):
    print(args[::2])
    for i in kwargs.values():
        if type(i) == str:
            print(i)


homeW(1, 2, 3, 5, 5, 8, 9, a=2, b='asf', g=8, t='afasf', y='12412')