import random

numbs = [random.randint(1, 10) for n in range(10)]
print(f'Массив: {numbs}')
numb = numbs[0]
max_count = 0

for i in range(len(numbs)):
    count = 0
    for j in range(len(numbs)):
        if numbs[i] == numbs[j]:
            count += 1
    if count > max_count:
        max_count = count
        numb = numbs[i]
if max_count > 1:
    print(f'Число "{numb}" встречается {max_count} раз(а).')
else:
    print('Все элементы уникальны')
