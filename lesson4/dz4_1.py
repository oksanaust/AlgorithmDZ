import time
import cProfile

# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.

# Первый вариант


def func_div1(numb):
    div_dict = dict()
    for div in range(2, 10):
        div_dict[div] = 0
        for numb in range(2, numb + 1):
            if numb % div == 0:
                div_dict[div] += 1
    return div_dict


time_start = time.time()
print(func_div1(999999))
time_finish = time.time()
print(time_finish - time_start, 'секунд')
cProfile.run('func_div1(999999)')
# cProfile.run('func_div1()')
# 1    0.000    0.000    0.000    0.000 dz4_1.py:10(func_div1)  99
# 1    0.005    0.005    0.005    0.005 dz4_1.py:10(func_div1)  999
# 1    0.025    0.025    0.025    0.025 dz4_1.py:10(func_div1)  9999
# 1    0.252    0.252    0.252    0.252 dz4_1.py:10(func_div1)  99999
# 1    2.013    2.013    2.013    2.013 dz4_1.py:10(func_div1)  999999
# Измерение времени через модуль time показал:
# func_div1(99):     0.0 секунд
# func_div1(999):    0.0030 секунд
# func_div1(9999):   0.0311 секунд
# func_div1(99999):  0.3250 секунд
# func_div1(999999): 2.5700 секунд
# Алгоритм работает достаточно быстро при небольших значениях входных данных. Может нуждаться в оптимизации
# в случае частого использования и больших значениях входных данных.
# Алгоритм работает приблизительно за O(n).

print('*' * 100)
# Второй вариант


def func_div2(numb):
    div_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for num in range(2, numb + 1):
        if num % 2 == 0:
            div_dict[2] += 1
        if num % 3 == 0:
            div_dict[3] += 1
        if num % 4 == 0:
            div_dict[4] += 1
        if num % 5 == 0:
            div_dict[5] += 1
        if num % 6 == 0:
            div_dict[6] += 1
        if num % 7 == 0:
            div_dict[7] += 1
        if num % 8 == 0:
            div_dict[8] += 1
        if num % 9 == 0:
            div_dict[9] += 1
    return div_dict


time_start = time.time()
print(func_div2(999999))
time_finish = time.time()
print(time_finish - time_start, 'секунд')
cProfile.run('func_div2(999999)')
# cProfile.run('func_div2()')
# 1    0.000    0.000    0.000    0.000 dz4_1.py:45(func_div2)  99
# 1    0.005    0.005    0.005    0.005 dz4_1.py:45(func_div2)  999
# 1    0.025    0.025    0.025    0.025 dz4_1.py:45(func_div2)  9999
# 1    0.216    0.216    0.216    0.216 dz4_1.py:45(func_div2)  99999
# 1    1.201    1.201    1.201    1.201 dz4_1.py:45(func_div2)  999999
# Измерение времени через модуль time показал:
# func_div2(99):     0.0 секунд
# func_div2(999):    0.0050 секунд
# func_div2(9999):   0.0299 секунд
# func_div2(99999):  0.2500 секунд
# func_div2(999999): 1.4000 секунд
# Алгоритм ведет себя примерно так же, как и первый вариант, чуть быстрее.
# Алгоритм работает приблизительно за O(n).

print('*' * 100)
# Третий вариант


def func_div3(numb):
    div_dict = dict()
    for div in range(2, 10):
        div_dict[div] = numb // div
    return div_dict


time_start = time.time()
print(func_div3(999999))
time_finish = time.time()
print(time_finish - time_start, 'секунд')
cProfile.run('func_div3(999999)')
# cProfile.run('func_div3()')
# 1    0.000    0.000    0.000    0.000 dz4_1.py:91(func_div3)  99
# 1    0.000    0.000    0.000    0.000 dz4_1.py:91(func_div3)  999
# 1    0.000    0.000    0.000    0.000 dz4_1.py:91(func_div3)  9999
# 1    0.000    0.000    0.000    0.000 dz4_1.py:91(func_div3)  99999
# 1    0.000    0.000    0.000    0.000 dz4_1.py:91(func_div3)  999999
# Измерение времени через модуль time показал те же результаты.
# Алгоритм работает быстро, в оптимизации не нуждается
# Алгоритм работает приблизительно за O(1).

# Вывод из 3-х вариантов реализации программы лучше себя показывает третий вариант по времени и лаконичности кода.
