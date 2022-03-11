from random import randint

n = int(input('Введите количество элементов: '))
mass = [randint(0, 100) for n in range(n)]
max_numb = mass[0]
min_numb = mass[0]
print(mass)

for n in mass:
    if n > max_numb:
        max_numb = n
    elif n < min_numb:
        min_numb = n
# min_numb = min(mass)
# max_numb = max(mass)
min_index = mass.index(min_numb)
max_index = mass.index(max_numb)
mass[max_index], mass[min_index] = mass[min_index], mass[max_index]

print(f'Минимальный элемент массива {min_numb} находится на {min_index + 1} месте (индекс {min_index}).\n'
      f'Максимальный элемент массива {max_numb} находится на {max_index + 1} месте (индекс {max_index}).')
print(f'Меняем местами эти элементы:\n{mass}')
