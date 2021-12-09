product = { 'Морожное': [['молоко восстановленное', 'глазурь жировая какаосодержащая', 'молокo', 'пудра  сахарная', 'какао-порошок', 'сироп крем-брюле', 'сахар', 'вода', 'масло', 'молоко сухое'], [2, 18, 10, 16, 6, 14, 8, 12, 10, 10,], 120, 30],
            'торт': [['Кефир', 'Яйца СО', 'Сахар', 'Мука', 'Какао-порошок', 'Творог', 'Сметана', 'Сахар',  'Ванильный сахар', 'Сметана'], [20, 180, 100, 160, 60, 140, 80, 120, 100, 100], 4000, 15],
            'маффин': [['Мука пшеничная', 'Сахар', 'Сливочное масло', 'Молоко', 'Какао-порошок', 'Яйцо', 'Мускатный орех', 'Растительное масло', 'Ванин', 'Ягоды'], [1, 9, 5, 7, 3, 6, 4, 6, 5, 4], 50, 22],
            'пирожное': [['Вода', 'Молоко', 'Масло сливочное', 'Мука пшеничная', 'Яйцо куриное', 'Соль', 'Сахар коричневый', 'Ванилин', 'Тесто слоеное'], [3, 27, 15, 21, 9, 18, 12, 18, 15, 12], 150, 20]}
def kol_tov():
    while True:
        x = input('введите количество товара')
        try:
            if (type(int(x))) == int:
                return(x)
                break
        except ValueError:
            if x == 'n':
                return (x)
                break
            continue
        else:
            continue

def pokupki():
    pok = dict()
    while True:
        for i in enumerate(product.keys()):
            print(f'{i[0]+1} - {i[1]}')
        print(f'n - выход\n{"_"*10}')
        if pok != {}:
            sum = 0
            for key, value in pok.items():
                print(f'Вы купили товар {key} в количестве {value} на сумму {value*product[key][2]} рублей.')
                print(f'В магазине осталось {key} - {product[key][3]-value} шт.')
                sum += value*product[key][2]
            print(f'Итоговая сумма равна {sum}')
        x = input('выберите товар который хотите купить:')
        if x == 'n':
            return(pok)
            break
        elif x.isalpha():
            continue
        elif (type(int(x)) == int) and (int(x)<=len(product)):
            for i in enumerate(product.keys()):
                if int(x)-1 == i[0]:
                    if i[1] in pok:
                        temp = pok[i[1]] + int(kol_tov())
                        if (product[i[1]][3]) >= temp:
                            pok[i[1]] = temp
                        else:
                            print('Такого количества нет в кафе')
                            continue
                    else:
                        pok[i[1]] = int(kol_tov())
        else:
            continue

while True:
    user_choice = input('1 - посмотреть описание\n2 - посмотреть цену\n3 - посмотреть количество\n4 - Всю информацию\n5 - Приступить к покупке\n6 - Выход')
    if user_choice == '1':
        print('В кофе есть cледующие десерты:')
        for key, value in product.items():
            print(f'{"_"*10}\n{key}')
            for i in value[0]:
                print(f'{i} - 100грамм продукта содержиться {value[1][value[0].index(i)]} грамм')
        print(f'{"_"*10}')
    elif user_choice == '2':
        for key, value in product.items():
            print(f'{"_"*10}\n{key}\nСтоимость {value[2]} рублей.')
        print(f'{"_"*10}')
    elif user_choice == '3':
        for key, value in product.items():
            print(f'{"_" * 10}\n{key}\nКолличество в магазине {value[3]} штук.')
        print(f'{"_" * 10}')
    elif user_choice == '4':
        print('В кофе есть cледующие десерты:')
        for key, value in product.items():
            print(f'{"_" * 10}\n{key}')
            for i in value[0]:
                print(f'{i} - 100грамм продукта содержиться {value[1][value[0].index(i)]} грамм')
            print(f'по стоимости {value[2]} рублей\nв колличестве {value[3]} шт.')
        print(f'{"_" * 10}')

    elif user_choice == '5':
        pok = pokupki()
        print(pok)
    elif user_choice == '6':

        print('Спасибо что посетили наш магазин')