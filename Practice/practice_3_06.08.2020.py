# Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове.
# (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а также сколько всего букв в слове, сколько гласных и согласных.
a = 'аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY'
b = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩbcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
upper = 'АЕЁИОУЫЭЮЯБВГДЖЗЙКЛМНПРСТФХЦЧШЩAEIOUYBCDFGHJKLMNPQRSTVWXZ'
lower = 'аеёиоуыэюяaeiouyбвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz'
glas = 0
soglas = 0
amount_low = 0
amount_up = 0
print('Введите слово для анализа:')
word = input()
for i in word:
    if i in a:
        glas += 1
    elif i in b:
        soglas += 1
for k in range(1, len(word)):
    if word[k - 1].islower() and word[k].islower():
        amount_low += 1
    if word[k - 1].isupper() and word[k].isupper():
        amount_up += 1
print('\n', f'Количество символов в введенном слове: {len(word)}', '\n', f'Гласных букв в слове: {glas}', '\n',
      f'Согласных букв в слове: {soglas}', '\n',
      f'Количество пар символов верхнего регистра, стоящих рядом: {amount_up}',
      '\n', f'Количество пар символов верхнего регистра, стоящих рядом: {amount_low}')
