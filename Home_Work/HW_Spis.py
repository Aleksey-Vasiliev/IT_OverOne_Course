spis = ['one', 'two', 2, 6, [7, 8, 9], 'good']
b = [1, 2, 3]
sum = 0
spis[0] = b
for i in b:
    sum += i
spis.append(sum)
print(spis)
