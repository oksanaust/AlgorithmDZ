import random

numbs = [random.randint(0, 100) for numb in range(10)]
print(f'Массив: {numbs}')
min_index = 0
max_index = 9
sum_numb = 0

for n in numbs:
    if numbs[min_index] > n:
        min_index = numbs.index(n)
    if numbs[max_index] < n:
        max_index = numbs.index(n)

print(f'Минимальное число "{numbs[min_index]}" находится на позиции {min_index}')
print(f'Максимальное число"{numbs[max_index]}" находится на позиции {max_index}')

for i in range(len(numbs)):
    if min_index > i > max_index or min_index < i < max_index:
        sum_numb = sum_numb + numbs[i]
        i += 1
print(f'Сумма элементов, находящихся между минимальным и максимальным элементами = {sum_numb}')
