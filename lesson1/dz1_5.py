print('Введите две буквы латинского алфавита:')
letter1 = input('letter1: ').lower()
letter2 = input('letter2: ').lower()

pos_letter1 = ord(letter1) - 96
pos_letter2 = ord(letter2) - 96
distance = abs(pos_letter1 - pos_letter2) - 1
print(f'Буква "{letter1}" {pos_letter1}-я в алфавите\n'
      f'Буква "{letter2}" {pos_letter2}-я в алфавите\n'
      f'Между буквами {distance} букв')
