with open('12.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        print(f'Вывод строки - {line}')
