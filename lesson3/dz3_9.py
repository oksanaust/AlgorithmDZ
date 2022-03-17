from random import randint

print('Для создания матрицы введите количество столбцов (x) и строк (y):')
x = int(input('x = '))
y = int(input('y = '))
print()

arr = [[randint(1, 100) for i in range(x)] for j in range(y)]
min_lst = [min(arr[i][j] for i in range(y)) for j in range(x)]
for a in arr:
    print(('{:4d} ' * len(a)).format(*a))
    i = 0
    for j in a:
        if j < min_lst[i]:
            min_lst[i] = j
        i += 1

print('-' * x * 5)
print(('{:4d} ' * len(min_lst)).format(*min_lst))
print()

min_lst.sort()
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {min_lst[0]}')
