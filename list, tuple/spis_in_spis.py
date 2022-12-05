# a = [1, 2, 3, 4, ['hello', 'a', 12], 5]
# print(a[4])
A = [[1, 2, 3],[4, 5, 6, 7], 'hello']
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end = '')