import random

numbs = [random.randint(-10, 10) for numb in range(10)]
print(f'Массив: {numbs}')
index = 0

for n in numbs:
    if numbs[index] > n:
        index = numbs.index(n)

if numbs[index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'Минимальный отрицательный элемент в массиве "{numbs[index]}" находится на позиции {index}')
