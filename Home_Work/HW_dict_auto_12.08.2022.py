# Значениями словаря могут быть и списки.
# Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений.
# Выведите первое и последнее значения каждого из ключей.
print('Задача № 1')

auto = {'BMW':['M3', 'X5', 'X7'], 'Tesla': ['Model S', 'Model E', 'Model X']}
for i in auto.values():
    print(f'{i[0]},', f'{i[-1]}.')
print()

# Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
print('Задача № 2')

slovar = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7}
multi = 1
for i in slovar.values():
    multi *= i
print(multi)

