# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это
# цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


def sum_hex(hex1, hex2):
    result = deque()
    rel = 0
    if len(hex2) > len(hex1):
        hex1, hex2 = deque(hex2), deque(hex1)
    else:
        hex1, hex2 = deque(hex1), deque(hex2)
    while hex1:
        if hex2:
            res = hex_numb[hex1.pop()] + hex_numb[hex2.pop()] + rel
        else:
            res = hex_numb[hex1.pop()] + rel
        rel = 0
        if res < 16:
            result.appendleft(hex_numb[res])
        else:
            result.appendleft(hex_numb[res - 16])
            rel = 1
    if rel:
        result.appendleft('1')
    return list(result)


def mul_hex(hex1, hex2):
    result = deque()
    spam = deque([deque() for _ in range(len(hex2))])
    hex1, y = hex1.copy(), deque(hex2)
    for i in range(len(hex2)):
        m = hex_numb[y.pop()]
        for j in range(len(hex1) - 1, -1, -1):
            spam[i].appendleft(m * hex_numb[hex1[j]])
        for _ in range(i):
            spam[i].append(0)
    rel = 0
    for _ in range(len(spam[-1])):
        res = rel
        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()
        if res < 16:
            result.appendleft(hex_numb[res])
        else:
            result.appendleft(hex_numb[res % 16])
            rel = res // 16
    if rel:
        result.appendleft(hex_numb[rel])
    return list(result)


h1 = list(input('Введите 1-е шестнадцатиричное число: ').upper())
h2 = list(input('Введите 2-е шестнадцатиричное число: ').upper())

hex_numb = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
            0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
            10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

print(*h1, '+', *h2, '=', *sum_hex(h1, h2))
print(*h1, '*', *h2, '=', *mul_hex(h1, h2))