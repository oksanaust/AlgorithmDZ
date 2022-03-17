from random import randint


def sum_numbs(number):
    sum_numb = 0
    for f in number:
        sum_numb += int(f)
    return sum_numb


n = int(input('Количество случайных натуральных чисел (n): '))
numbs = [str(randint(1, 1000)) for i in range(n)]

max_numb = 0
max_sum = 0
for i in numbs:
    if sum_numbs(i) > max_sum:
        max_numb = i
        max_sum = sum_numbs(i)
string = ', '.join(numbs)
print(f'Из последовательности ({string}), у числа {max_numb} была наибольшая сумма цифр - {max_sum}')
