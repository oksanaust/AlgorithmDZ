# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
# и отсортированный массивы. Сортировка должна быть реализована в виде функции.

from random import randint
import time
import sys


def bubble_sort(lst):
    swapped = False
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return lst


size = int(input('Введите размер массива: '))
time_start = time.time()
my_lst = [randint(-100, 99) for i in range(size)]
res = bubble_sort(my_lst)
time_finish = time.time()

print(f'Массив:\n{my_lst}')
print(f'Отсортированный массив:\n{res}')
print(f'Время работы алгоритма {time_finish - time_start} секунд.')

sum_member = sys.getsizeof(size) + sys.getsizeof(my_lst) + sys.getsizeof(bubble_sort(my_lst))
print(f'Затраты памяти на переменные: {sum_member}')

# Введите размер массива: 10
# Время работы алгоритма 0.0 секунд.
# Затраты памяти на переменные: 412
# Введите размер массива: 100
# Время работы алгоритма 0.0050 секунд.
# Затраты памяти на переменные: 1852
# Введите размер массива: 1000
# Время работы алгоритма 0.5600 секунд.
# Затраты памяти на переменные: 18076
# Алгоритм работает приблизительно за O(n**2).
# Пространственная сложность соответствует O(n**2).
