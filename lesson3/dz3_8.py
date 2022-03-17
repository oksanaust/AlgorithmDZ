from random import randint

print('Для создания матрицы 4*4 введите диапазон случайных чисел (a, b):')
a = int(input('a = '))
b = int(input('b = '))
arr = []

for i in range(4):
    lst = []
    for j in range(4):
        lst.append(int(randint(a, b)))
        print(f'{lst[j]:4}', end='')
    arr.append(lst)
    print(' |', sum(lst))
