# Условия задач
# 1. Даны вещественные положительные числа a, b, c. Необходимо выяснить, существует ли треугольник со сторонами a, b, c.
# 2. Дано целое число n (n находится в диапазоне от 1 до 99), определяющее возраст человека в годах.
# Для этого числа необходимо напечатать фразу "мне n лет".
# Учитывайте, что при некоторых значениях n слово "лет" нужно заменить на слово "год" или "года".

a = float(input('Введине первую сторону треугольника: '))
b = float(input('Введине вторую сторону треугольника: '))
c = float(input('Введине третью сторону треугольника: '))

if a+b>c and b+c>a and c+a>b:
    print('Треугольник с такими сторонами существует.')
else:
    print('Треугольника с такими сторонами не существует.')\


