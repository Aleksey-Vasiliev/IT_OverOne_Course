# 'ab' - сокращение от address book

ab = {'Swaroop':'swaroop@swaroopch.com', 'Larry':'larry@wawll.org',
      'Matsurmoto' : 'matz@ruby-lang.org', 'Spammer' : 'spammer@hotmail.com'}
print("Адрес Swaroop'a:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab ['Spammer']

# Вывод количества контактов в адресной книге и вывод всех адресов
print('\nВ адресной книге {} контакта\n'.format(len(ab)))

for name, address in ab.items():
      print('Контакт {} с адресом {}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
      print(f"Добавленный вручную контакт Guido с адресом {ab['Guido']}")