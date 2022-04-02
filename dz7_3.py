#  Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
#  Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
#  в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
#  Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
#  то используйте метод сортировки, который не рассматривался на уроках

from random import randint
import time
import sys


def med_arr(arr):
    for i in range(len(arr) - 1):
        left = 0
        right = 0
        equal = 0
        for j in range(len(arr)):
            if i != j:
                if arr[i] > arr[j]:
                    left += 1
                elif arr[i] < arr[j]:
                    right += 1
                elif arr[i] == arr[j]:
                    equal += 1
        if left == right:
            return arr[i]


size = int(input('Введите размер части массива: '))
min_numb = int(input('Введите минимальное значение массива: '))
max_numb = int(input('Введите максимальное значение массива: '))
time_start = time.time()
my_arr = [randint(min_numb, max_numb) for i in range(size * 2 + 1)]
res = sorted(my_arr)

print(f'Массив:\n{my_arr}')
print(f'Медиана: {med_arr(my_arr)}')
print(f'Отсортированный массив(для проверки):\n{res}')

time_finish = time.time()
print(f'Время работы алгоритма {time_finish - time_start} секунд.')

sum_member = sys.getsizeof(size) + sys.getsizeof(min_numb) + sys.getsizeof(max_numb) + sys.getsizeof(my_arr) + \
             sys.getsizeof(med_arr(my_arr)) + sys.getsizeof(res)
print(f'Затраты памяти на переменные: {sum_member}')

# Введите размер части массива:  size = 5, min_numb = 1, max_numb = 100
# Время работы алгоритма 0.0 секунд.
# Затраты памяти на переменные: 512
# Введите размер части массива:  size = 10, min_numb = 1, max_numb = 100
# Время работы алгоритма 0.0 секунд.
# Затраты памяти на переменные: 672
# Введите размер части массива:  size = 20, min_numb = 1, max_numb = 100
# Время работы алгоритма 0.0049 секунд.
# Затраты памяти на переменные: 1024
# Введите размер части массива:  size = 50, min_numb = 1, max_numb = 100
# Время работы алгоритма 0.0100 секунд.
# Затраты памяти на переменные: 2040
# Алгоритм работает приблизительно за O(n).
# Пространственная сложность ближе к O(n).
