a = [4, 6, 'py', 'tell', 78]
b = [44, 'hello', 56, 'expert', ['world', 5.7], 3, 6]
unit_spis = a + b #В видео к ДЗ необходимо сложить списки двумя способами.
a.extend(b)
a.insert(3,a[5])
# Поставил первым парметром 3, а не 2, так как в условиях нужно на третью позицию поставить 6 элемент, считаю что
# позиция это при индексировании, а шестой элемент это по счёту, при этом счёт начинаем с единицы, но по индексации
# шестой элемент имеет индекс 5, поэтому второй параметр это 5, а вообще как ТЗ написано, так и сделано =).
print('\n', 'Результат сложения списков: ', '\n', unit_spis, '\n', 'На 3 позицию списка поставлен 6 элемент списка: ',
      '\n', a, '\n', 'Количество повторений числа 6 в списке:',a.count(6),'\n', 'Количество элементов в списке:',
      len(a),'\n', 'Первым элементом вложенного списка является:', a[10][0])

