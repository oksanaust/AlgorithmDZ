# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

import time
import cProfile

n = int(input("Введите номер простого числа, которое хотите увидеть: "))
# Используя алгоритм «Решето Эратосфена»


def eratosthenes_sieve(numb):
    k = numb * 20
    a = [i for i in range(k + 1)]
    a[1] = 0
    i = 2
    while i <= k:
        if a[i] != 0:
            j = i + i
            while j <= k:
                a[j] = 0
                j = j + i
        i += 1
    a = [i for i in a if a[i] != 0]
    for numb in range(len(a)):
        if numb == n:
            return f'{n}-е простое число = {a[numb - 1]}'


time_start = time.time()
print(eratosthenes_sieve(n))
time_finish = time.time()
print('*' * 150)
print(time_finish - time_start, 'секунд')
cProfile.run('eratosthenes_sieve(1000)')
# cProfile.run('eratosthenes_sieve()')
# 1    0.000    0.000    0.000    0.000 dz4_2.py:13(eratosthenes_sieve)  1
# 1    0.000    0.000    0.000    0.000 dz4_2.py:13(eratosthenes_sieve)  10
# 1    0.003    0.003    0.004    0.004 dz4_2.py:13(eratosthenes_sieve)  100
# 1    0.033    0.033    0.040    0.040 dz4_2.py:13(eratosthenes_sieve)  1000
# 1    0.324    0.324    0.396    0.396 dz4_2.py:13(eratosthenes_sieve)  10000
# Измерение времени через модуль time показал:
# eratosthenes_sieve(1):      0.0 секунд
# eratosthenes_sieve(10):     0.0 секунд
# eratosthenes_sieve(100):    0.0049 секунд
# eratosthenes_sieve(1000):   0.0449 секунд
# eratosthenes_sieve(10000):  0.4460 секунд
# Алгоритм работает достаточно быстро и в оптимизации не нуждается
# Алгоритм работает приблизительно за O(log(n)).

# Без использования «Решета Эратосфена»


def prime_numb(numb):
    prime_lst = []
    k = numb * 20
    for i in range(1, k + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_lst.append(i)
    for prime in range(len(prime_lst)):
        if prime == numb:
            return f'{numb}-е простое число = {prime_lst[prime - 1]}'


time_start = time.time()
print(prime_numb(n))
time_finish = time.time()
print('*' * 150)
print(time_finish - time_start, 'секунд')
cProfile.run('prime_numb(1000)')
# cProfile.run('prime_numb()')
# 1    0.000    0.000    0.000    0.000 dz4_2.py:55(prime_numb)  1
# 1    0.001    0.001    0.001    0.001 dz4_2.py:55(prime_numb)  10
# 1    0.088    0.088    0.088    0.088 dz4_2.py:55(prime_numb)  100
# 1    3.704    3.704    3.705    3.705 dz4_2.py:55(prime_numb)  1000
# 1  145.947  145.947  145.954  145.954 dz4_2.py:55(prime_numb)  10000
# Измерение времени через модуль time показал:
# prime_numb(1):      0.0 секунд
# prime_numb(10):     0.0049 секунд
# prime_numb(100):    0.0870 секунд
# prime_numb(1000):   4.5350 секунд
# prime_numb(10000):  149.7425 секунд
# Увеличение количества чисел в 10 раз увеличивает время выполнения приблизительно в 100 раз.
# Это означает, что алгоритм работает приблизительно за O(n**2). Не самый лучший вариант.

# Вывод из 2-х вариантов реализации программы лучшее время в данном случае показывает алгоритм «Решето Эратосфена».
