import random

numbs = [random.randint(0, 100) for numb in range(10)]
print(f'Массив: {numbs}')
min_numb = min(numbs[0], numbs[1])
sec_min = max(numbs[0], numbs[1])
for n in range(2, len(numbs)):
    if numbs[n] <= min_numb:
        sec_min = min_numb
        min_numb = numbs[n]
    else:
        if numbs[n] <= sec_min:
            sec_min = numbs[n]
print(f'Два наименьших элемента массива равны "{min_numb}" и "{sec_min}"')
