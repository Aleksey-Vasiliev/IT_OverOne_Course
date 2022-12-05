# a = ()
# b = tuple([1, 2, 3, 4, 5, 6])
# print(b)
# print(type(b))

import random
a = [random.randint(1,200) for i in range(10)]
a = tuple(a)
print(a, '\n', a.index(max(a)), a.index(min(a)))
