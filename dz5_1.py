# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

numb_firm = int(input('Введити кол-во компаний для анализа: '))
year = 0
total = 0
firms = {}

for i in range(numb_firm):
    name = input(f'Название {i + 1}-й компании: ')
    quart = [float(input(f'Прибыль за {j+1} квартал: ')) for j in range(4)]
    year = sum(quart)
    firms[name] = year
    total += year
total_middle = total / numb_firm
print(firms)
print()

print(f'Компания с прибылью выше средней {total_middle:.2f}: ')
for k, v in firms.items():
    if v >= total_middle:
        print(f'"{k}" получила годовую прибыль {v} ед.')
print()

print(f'Компания с прибылью ниже средней {total_middle:.2f}: ')
for k, v in firms.items():
    if v < total_middle:
        print(f'"{k}" получила годовую прибыль {v} ед.')

# Алгоритм работает приблизительно за O(n).
