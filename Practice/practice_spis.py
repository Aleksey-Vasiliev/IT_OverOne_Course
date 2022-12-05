# Список из 7 цифр. Если четных больше, чем нечетных, то найти сумму всех цифр.
# Если нет, то произведение 1,3 и 6 элемента
import random
spis = []
chet = 0
ne_chet = 0
result = 0
for i in range(7):
    i = random.randint(1, 200)
    spis.append(i)
    if i % 2 == 0:
        chet += 1
    else:
        ne_chet += 1
if chet > ne_chet:
    for i in spis:
        result += i # Можно использовать функцию 'sum' result = sum(spis)
else:
    result = spis[0] * spis[2] * spis[5]
print('Сгенерированный список: ', spis, '\n'
      'Количество четных чисел: ', chet, '\n'
      'Количество нечетных чисел: ', ne_chet, '\n'
      'Результат: ', result)

