from random import randint

n = int(input('Введите количество элементов: '))
ind = []
numb = []
mass = [randint(0, 100) for n in range(n)]
print(mass)

for i in range(len(mass)):
    if mass[i] % 2 == 0:
        ind.append(i)
        numb.append((i + 1))
print(f'Индексы четных элементов массива {ind}\nили номер п/п в списке {numb}')
