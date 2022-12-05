class HW:
    '''Если передают строку, то смотрим: если произведение гласных и согласных букв меньше или равно длине слова,
    выводить все гласные, иначе согласные; если число то, произведение суммы чётных цифр на длину числа.

    Длину строки и числа искать во втором методе'''

    def __init__(self):
        self.inp()

    def inp(self):
        self.a = input('Введите строку, либо число, либо - для выхода: ')

    def func(self):
        if self.a.isdigit():
            even = 0
            ev = '24680'
            for i in self.a:
                if i in ev:
                    even += int(i)
            return f'Произведение суммы чётных цифр на длину числа: {even * len(self.a)}'
        if self.a.isalpha():
            vow = ''
            con = ''
            vowels = 0
            consonants = 0
            letter = 'eyuioaуеыаоэяию'
            for i in self.a.lower():
                if i in letter:
                    vowels += 1
                    vow += i
                else:
                    consonants += 1
                    con += i
            if vowels * consonants <= len(self.a):
                return f'Гласные: {vow}'
            else:
                return f'Согласные: {con}'

    def ln(self):
        return f'Длина: {len(self.a)}'


while True:
    ex = HW()
    if ex.a == '-':
        break
    print(ex.func())
    print(ex.ln())
