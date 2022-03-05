n = int(input('Введите количество элементов ряда чисел, из которых будет складываться сумма: '))

el = 1
sum_el = 0
while n > 0:
    print(el, end=' ')
    sum_el += el
    el /= -2
    n -= 1
print(f'\nСумма {sum_el}')
