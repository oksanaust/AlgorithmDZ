print('Для определения был ли год високосным, введите год:')
user_year = int(input('year = '))

if user_year % 4 == 0 and user_year % 100 != 0 or user_year % 400 == 0:
    print(f'{user_year} год - високосный')
else:
    print(f'{user_year} год - невисокосный')
