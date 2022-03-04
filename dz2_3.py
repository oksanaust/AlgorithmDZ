number = int(input('Введите любое число: '))

revers = 0
while number != 0:
    div = number % 10
    revers = revers * 10 + div
    number = number // 10
print(revers)
