i = 1
for el in range(32, 128):
    if i % 10 == 0:
        print(f'{el:6} : {chr(el)}')
    else:
        print(f'{el:6} : {chr(el)}', end='')
    i += 1
