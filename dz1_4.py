from random import randint, uniform

user_choice = input('Если вы хотите сгенерировать случайное целое число, нажмите "n",\n'
                    'если случайное вещественное число - "f", если случайную букву - "l": ')
if user_choice == 'n':
    print('Введите границы (диапазон) для случайного целого числа (n1, n2):')
    n1 = int(input('n1 = '))
    n2 = int(input('n2 = '))
    rand_int = randint(n1, n2)
    print(f'Случайное целое число: {rand_int}')
elif user_choice == 'f':
    print('Введите границы (диапазон) для случайного вещественного числа (f1, f2):')
    f1 = float(input('f1 = '))
    f2 = float(input('f2 = '))
    rand_float = uniform(f1, f2)
    print(f'Случайное вещественное число: {rand_float}')
elif user_choice == 'l':
    print('Введите границы (диапазон) для любой случайной буквы (l1, l2):')
    l1 = input('l1 = ').lower()
    l2 = input('l2 = ').lower()
    rand_letter = chr(randint(ord(l1), ord(l2)))
    print(f'Случайная буква: {rand_letter}')
