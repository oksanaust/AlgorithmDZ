# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
# и отсортированный массивы.

from random import randint
import time
import sys


def merge_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    else:
        middle = int(len(lst) / 2)
        left = merge_sort(lst[:middle])
        right = merge_sort(lst[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result


size = int(input('Введите размер массива: '))
time_start = time.time()
my_lst = [randint(0, 49) for i in range(size)]
res = merge_sort(my_lst)
time_finish = time.time()

print(f'Массив:\n{my_lst}')
print(f'Отсортированный массив:\n{res}')
print(f'Время работы алгоритма {time_finish - time_start} секунд.')

sum_member = sys.getsizeof(size) + sys.getsizeof(my_lst) + sys.getsizeof(merge_sort(my_lst))
print(f'Затраты памяти на переменные: {sum_member}')

# Введите размер массива: 10
# Время работы алгоритма 0.0 секунд.
# Затраты памяти на переменные: 412
# Введите размер массива: 100
# Время работы алгоритма 0.0 секунд.
# Затраты памяти на переменные: 1852
# Введите размер массива: 1000
# Время работы алгоритма 0.0399 секунд.
# Затраты памяти на переменные: 18076
# Алгоритм работает приблизительно за O(n).
# Пространственная сложность соответствует O(n**2).
