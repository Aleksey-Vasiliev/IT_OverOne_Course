a = [5, 2, 4, 4, 5, 1, 4, 5, 5, 3, 6, 2, 3, 77, 43, -3, -5, -99, -99, -99, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 8, 9, 8, 9]
a.sort()
print(a)
for i in a:
    if a.count(i) > 1:
        for k in range (a.count(i)-1):
            a.remove(i)
print(a)














