# Два метода в классе, один принимает в себя либо строку, либо число.
# Если передают строку, то смотрим: если произведение гласных и согласных букв меньше или равно длине слова,
# выводить все гласные, иначе согласные; если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе

class Str_or_numb:
    def meth_1(self):
        a = input("Введите строку либо число: ")

    def meth_2(self):
        dlina = len(a)
