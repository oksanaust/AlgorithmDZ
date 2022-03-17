def func_sum(numb):
    if numb == 1:
        return numb
    elif numb > 1:
        return numb + func_sum(numb - 1)


def func_mul(numb):
    return numb * (numb + 1) // 2


n = int(input('Введите любое натуральное число (n): '))

if func_sum(n) == func_mul(n):
    print(f'Для n = {n} - выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число')
else:
    print(f'Для n = {n} - равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число, не выполняется')
