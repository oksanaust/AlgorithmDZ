from random import randint

n = int(input('Количество случайных чисел в последовательности (n): '))
numb = input('Цифра, у которой необходимо посчитать количество вхождений в данную последовательность: ')

numbs = [randint(0, 1000) for i in range(n)]
numbs = str(numbs)
count = 0

for el in numbs:
    for x in el:
        if x == numb:
            count += 1
        # count = numbs.count(numb)
print(f'Цифра "{numb}" встречается в последовательности чисел {numbs}: {count} раз(а)')
