# Выведи на экран все числа в диапазоне от 54 до 9184 кратные 5 (решить через for)
ost = 0
for i in range(54,9184):
    ost = i % 5
    if ost == 0:
        print(i)