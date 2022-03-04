while True:
    print('Введите два числа:')
    a = float(input('a = '))
    b = float(input('b = '))
    symbol = input("Введите знак операции, это может быть знак: '+', '-', '*', '/'. Для выхода нажмите '0': ")

    while symbol != '0' and symbol != '+' and symbol != '-' and symbol != '/' and symbol != '*':
        print('Введен недопустимый знак операции.')
        symbol = input("Введите знак операции, это может быть знак: '+', '-', '*', '/'. Для выхода нажмите '0': ")
    else:
        if symbol == '0':
            print('Выход')
            break
        elif symbol == '+':
            print(f'{a} {symbol} {b} = {a + b}')
        elif symbol == '-':
            print(f'{a} {symbol} {b} = {a - b}')
        elif symbol == '*':
            print(f'{a} {symbol} {b} = {a * b}')
        elif symbol == '/':
            if b == 0:
                print('Ошибка. Деление на ноль. Введите заново число b')
                b = float(input('b = '))
            print(f'{a} {symbol} {b} = {a / b}')
