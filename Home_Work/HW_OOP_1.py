# Два метода в классе, один принимает в себя либо строку, либо число.
# Если передают строку, то смотрим: если произведение гласных и согласных букв меньше или равно длине слова,
# выводить все гласные, иначе согласные; если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе

class Homework:
    def vvod(self, users_input):
        self.users_input = users_input
    def len_vvod(self, users_input):
        if users_input.isdigit() == True:
            users_input = int(users_input)
        dlina = len(str(users_input))
        glas = 'АУОИЭЫЯAEIOUY'
        soglas = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩBCDFGHJKLMNPQRSTVWXZ'
        glas_value = 0
        soglas_value = 0
        multiply = 1
        spis = ''
        if type(users_input) == str:
            for i in users_input:
                if i.upper() in glas:
                    glas_value += 1
                elif i.upper() in soglas:
                    soglas_value += 1
            if glas_value * soglas_value <= dlina:
                for i in users_input:
                    if i.upper() in glas:
                        spis = spis + i
            else:
                for i in users_input:
                    if i.upper() in soglas:
                        spis = spis = spis + i
        if type(users_input) == int:
            users_input = str(users_input)
            for i in users_input:
                if int(i)%2 == 0:
                    multiply *= int(i)
            multiply *= dlina
        if type(users_input) == str:
            print(spis)
        if users_input.isdigit() == True:
            print(multiply)
users_input = input('Введите строку или число: ')
ex = Homework()
ex.len_vvod(users_input)