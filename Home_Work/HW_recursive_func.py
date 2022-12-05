# Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке.
# Список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100

import random

my_spis = []
for i in range(10):
    my_spis.append(random.randint(1, 100))
print(my_spis)
def recursive():
    global sum_spis
    sum_spis = 0
    for i in my_spis:
        sum_spis += i
    print(sum_spis)
recursive()