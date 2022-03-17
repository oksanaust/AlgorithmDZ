from random import randint

numb = randint(0, 100)
count = 0
max_count = 10
print(f'Попробуйте угадать случайное число от 1 до 100, у вас есть {max_count} попыток. Начали! ')

while count < max_count:
    user_numb = int(input(f'Попытка №{(count + 1):2}. Введите число от 1 до 100: '))
    if user_numb == numb:
        print(f'Ура!!! Вы угадали с попытки №{(count + 1):2}! Это число {numb}')
        break
    elif user_numb > numb:
        print('Ваше число больше загаданного')
    else:
        print('Ваше число меньше загаданного')
    count += 1
else:
    print(f'К сожалению, у вас закончились попытки и вы проиграли! Загаданное число {numb}')
