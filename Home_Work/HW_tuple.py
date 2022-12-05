# import random
# a = [random.randint(0,9) for i in range(10)]
# a = tuple(a)
# print(a, '\n', sum(a))
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
print(long_word, '\n', 'В данной строке имеется', long_word.count('т'), 'символов Т', '\n',
      'В данной строке имеется', long_word.count('и'), 'символов И', '\n',
      'В данной строке имеется', long_word.count('а'), 'символов А')
print(type(long_word))


