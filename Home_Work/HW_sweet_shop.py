# Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов продукции, а также узнать её состав.
# Реализуйте кондитерскую. У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и т.д.).
# Значение – список, который содержит состав, цену (за 100гр) и кол-во (в граммах). Предложите выбор:
# 1. Если человек хочет посмотреть состав: название – состав
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке: С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке
# 6. До свидания.
amount_buy = 0
cost_buy = 0
const = ''
amount_1 = 1430
amount_2 = 1220
amount_3 = 930
amount_4 = 850
cost_1 = 2.5
cost_2 = 3
cost_3 = 4
cost_4 = 7

print(" Вас приветствует кондитерская 'SweetIT'\n Мы можем Вам предложить маффин, пирожное, торт и знаменитый на весь"
      " Тамриэль сладкий рулет!\n Вы можете узнать информацию о кондитерском изделии, а именно: состав, цену и "
      " количество, доступное для заказа.\n")
while True:
    name_prod = ['маффин', 'пирожное', 'торт', 'сладкий рулет']
    compound = [['Состав: вода, масло растительное, сахар тростниковый, мука, какао порошок.', f'Цена за 100 гр.'
                f' - {cost_1} руб. ', f'Имеется: {amount_1} гр.'], ['Состав: сахар-песок, белок яичный, масло'
                ' сливочное, молоко цельное сухое.', f'Цена за 100 гр. - {cost_2} руб.', f'Имеется: {amount_2} гр.'],
                [' Состав: мука, яйцо, сливки, шоколад, сахар.', f'Цена за 100 гр. - {cost_3} руб.', f'Имеется:'
                f' {amount_3} гр.'], ['Состав: сливочное масло, цельное молоко, мед, соль, яйцо, мука', f'Цена за'
                f' 100 гр. - {cost_4} руб.', f'Имеется: {amount_4} гр.']]
    production = dict(zip(name_prod, compound))
    prod_user = input(' Введите название интересующего Вас кондитерского изделия или Q для выхода из магазина,'
                      ' если хотите приступить к покупке, введите +: ')
    if prod_user.lower() == 'q':
        break
    elif prod_user == '+':
            prod_user = input(' Введите название кондитерского изделия, которое Вы желаете приобрести или введите'
                              ' Q для выхода из режима покупки: ')
            for i in name_prod:
                if prod_user.lower() == i and prod_user.lower() in name_prod:
                    prod_user = prod_user.lower()
                    if prod_user.lower() == "маффин" and amount_1 != 0:
                        parametr = int(input(" Введите количество в граммах, которое Вы желаете приобрести: "))
                        while const == '':
                            if parametr <= amount_1:
                                print(f' Стоимость вашей покупки составляет {cost_1 * parametr} руб.')
                                answer = input(f' Если вы желаете оплатить покупку'
                                               f' введите +, в противном случае введите любые данные.')
                                if answer == '+':
                                    cost_buy += parametr * cost_1
                                    amount_1 -= parametr
                                    production = dict(zip(name_prod, compound))
                                    print(' Спасибо за покупку!')
                                    break
                                else:
                                    break
                            else:
                                print(' В нашем магазине отсутвует такое количество выбранного Вами кондитерского'
                                     f' изделия. Вы можете заказать не более: {amount_1} гр.')
                                break
                    elif amount_1 == 0:
                        print(' Извините, но маффины кончились.')
                        break
                    elif prod_user.lower() == "пирожное" and amount_2 != 0:
                        parametr = int(input(" Введите количество в граммах, которое Вы желаете приобрести: "))
                        while const == '':
                            if parametr <= amount_2:
                                print(f' Стоимость вашей покупки составляет {cost_2 * parametr} руб.')
                                answer = input(f' Если вы желаете оплатить покупку'
                                               f' введите +, в противном случае введите любые данные.')
                                if answer == '+':
                                    cost_buy += parametr * cost_2
                                    amount_2 -= parametr
                                    production = dict(zip(name_prod, compound))
                                    print(' Спасибо за покупку!')
                                    break
                                else:
                                    break
                            else:
                                print(' В нашем магазине отсутвует такое количество выбранного Вами кондитерского'
                                     f' изделия. Вы можете заказать не более: {amount_2} гр.')
                                break
                    elif amount_2 == 0:
                        print(' Извините, но пирожные кончились.')
                        break
                    elif prod_user.lower() == "торт" and amount_3 != 0:
                        parametr = int(input(" Введите количество в граммах, которое Вы желаете приобрести: "))
                        while const == '':
                            if parametr <= amount_3:
                                print(f' Стоимость вашей покупки составляет {cost_3 * parametr} руб.')
                                answer = input(f' Если вы желаете оплатить покупку'
                                               f' введите +, в противном случае введите любые данные.')
                                if answer == '+':
                                    cost_buy += parametr * cost_3
                                    amount_3 -= parametr
                                    production = dict(zip(name_prod, compound))
                                    print(' Спасибо за покупку!')
                                    break
                                else:
                                    break
                            else:
                                print(' В нашем магазине отсутвует такое количество выбранного Вами кондитерского'
                                     f' изделия. Вы можете заказать не более: {amount_3} гр.')
                                break
                    elif amount_3 == 0:
                        print(' Извините, но торты кончились.')
                        break
                    elif prod_user.lower() == "сладкий рулет" and amount_4 != 0:
                        parametr = int(input(" Введите количество в граммах, которое Вы желаете приобрести: "))
                        while const == '':
                            if parametr <= amount_4:
                                print(f' Стоимость вашей покупки составляет {cost_4 * parametr} руб.')
                                answer = input(f' Если вы желаете оплатить покупку'
                                               f' введите +, в противном случае введите любые данные.')
                                if answer == '+':
                                    cost_buy += parametr * cost_4
                                    amount_4 -= parametr
                                    production = dict(zip(name_prod, compound))
                                    print(' Спасибо за покупку!')
                                    break
                                else:
                                    break
                            else:
                                print(' В нашем магазине отсутвует такое количество выбранного Вами кондитерского'
                                      f' изделия. Вы можете заказать не более: {amount_4} гр.')
                                break
                    elif amount_4 == 0:
                        print(' Извините, но скайримовские сладкие рулеты кончились.')
                        break
                elif prod_user.lower() == 'q':
                    break
                elif prod_user.lower() != i and prod_user.lower() not in name_prod:
                    print(' Вы ввели наименование, которое отсутвует в нашем меню, попробуйте снова.')
                    break
    elif prod_user.lower() in name_prod:
        while True:
            for i in name_prod:
                if prod_user.lower() == i and prod_user.lower() in name_prod:
                    prod_user = prod_user.lower()
                    parametr = input("\n Введите 'состав', 'цена' или 'количество' для получения соответствующей"
                                     " информации об изделии\n или введите пустую строку для получения всей информации"
                                     " об изделии. Введите Q для выхода из режима просмотра информации об изделии: ")
                    if parametr.lower() == 'состав':
                        print('', production[prod_user][0])
                    elif parametr.lower() == 'цена':
                        print('', production[prod_user][1])
                    elif parametr.lower() == 'количество':
                        print('', production[prod_user][2])
                    elif parametr.lower() == '':
                        result_str = ''
                        str_ = str(production[prod_user])
                        for i in str(production[prod_user]):
                            if i == '[':
                                continue
                            elif i == "'":
                                continue
                            elif i == ']':
                                continue
                            else:
                                result_str = result_str + i
                        print('', result_str, '\n')
                    elif parametr.lower() == 'q':
                        break
                    else:
                        print(' Вы ввели некоректный запрос. Попробуйте снова.', '\n')
            break
    else:
        print(' Вы ввели наименование, которое отсутвует в нашем меню, попробуйте снова.', '\n')
weight_ostatok = [amount_1, amount_2, amount_3, amount_4]
spis_ostatok =str(dict(zip(name_prod,weight_ostatok)))
result_spis = ''
for i in spis_ostatok:
    if i == '{':
        continue
    elif i == "'":
        continue
    elif i == '}':
        continue
    else:
        result_spis = result_spis + i
print(f' Сумма всех Ваших покупок составила: {cost_buy} руб.', '\n', f'В магазине осталась следующая продукция (гр.):'
      f' {result_spis}', '\n', 'До свидания!')