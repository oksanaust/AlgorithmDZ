from functools import reduce
from operator import mul

# Первый способ:
user_numb = input('Введите целое число: ')
numbers = [int(numb) for numb in user_numb]
while len(numbers) != 3:
    user_numb = input('Введите целое трёхзначное число: ')
    numbers = [int(numb) for numb in user_numb]
else:
    sum_numb = sum(numbers)
    mul_numb = reduce(mul, numbers)
    print(f'Сумма цифр из вашего числа равна {sum_numb} и произведение равно {mul_numb}')

# Второй способ:
# user_numb = input('Введите целое число: ')
# numbers = [int(numb) for numb in user_numb]
# while len(numbers) != 3:
#     user_numb = input('Введите целое трёхзначное число: ')
#     numbers = [int(numb) for numb in user_numb]
# else:
#     sum_numb = 0
#     mul_numb = 1
#     for i in numbers:
#         sum_numb += i
#         mul_numb *= i
#     print(f'Сумма цифр из вашего числа равна {sum_numb} и произведение равно {mul_numb}')
