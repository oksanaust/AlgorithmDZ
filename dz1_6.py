print('Введите номер желаемой буквы в латинском алфавите от 1 до 26:')
num_letter = int(input('number = '))

letter = chr(num_letter + 96)
print(f'Буква под номером {num_letter} - "{letter}"')
