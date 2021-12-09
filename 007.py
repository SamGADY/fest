while True:
    a = input('Введите число для деления на 100')
    try:
        d = 100/float(a)
        print(f' 100/{float(a)}= {d}')
    except ZeroDivisionError:
        continue
    except ValueError:
        continue
    finally:
        y = input('хотите продолжить n - выход, любая клавиша продолжить')
        if y == 'n':
            break
