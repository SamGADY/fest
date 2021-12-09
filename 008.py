with open('1.txt', 'r', encoding='utf-8') as f:

    famely = f.readline().replace('\n', '')
    famely = famely.replace(' ', '')
    name =  f.readline().replace('\n', '')
    name = name.replace(' ', '')
    ocen = f.readline().replace('\n', '')
    ocen = ocen.replace(' ', '')
    famely = famely.split(',')
    name = name.split(',')
    ocen = (ocen.split(','))
    print (ocen)
    for i in ocen:
        if i <= '3':
            print(f'Ученик {famely[ocen.index(i)]} {name[ocen.index(i)]} получил оченку {i}')
    #print(famely)
    print()
    #print(ocen)
