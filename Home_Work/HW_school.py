# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.

summa_ballov = 0
kol_strok = 0
with open('klass.txt', 'r', encoding='utf 8') as f:
    s = f.readlines()
    for i in s:
        kol_strok += 1
        i = i[:-1]
        summa_ballov += int(i[-1])
        if int(i[-1]) < 3:
            print(f'Оценка ниже трех баллов: {i[:-2]}')
print(f'Средний балл по классу: {summa_ballov/kol_strok}')