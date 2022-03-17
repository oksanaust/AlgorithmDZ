print('Введите 3 любых числа:')
num1 = float(input('num1 = '))
num2 = float(input('num2 = '))
num3 = float(input('num3 = '))

if num2 < num1 < num3 or num2 > num1 > num3:
    print(num1)
else:
    if num1 < num2 < num3 or num1 > num2 > num3:
        print(num2)
    else:
        print(num3)
