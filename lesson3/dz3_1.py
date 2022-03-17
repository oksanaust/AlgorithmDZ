for div in range(2, 10):
    numbs = []
    for numb in range(2, 100):
        if numb % div == 0:
            numbs.append(numb)
    print(f'Для числа {div} всего кратны - {len(numbs)} чисел.\nКратные числа: {numbs}.')
