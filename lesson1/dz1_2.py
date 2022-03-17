a = 5
b = 6

bit_and = a & b
bit_or = a | b
bit_xor = a ^ b
bit_shift_right = a >> 1
bit_shift_left = a << 2

print(f'Выполним логические побитовые операции над числами 5 и 6:\n'
      f'5 "И" 6 = {bit_and}\n'
      f'5 "ИЛИ" 6 = {bit_or}\n'
      f'5 "XOR" 6 = {bit_xor}\n'
      f'5 "Сдвиг вправо на" 1 = {bit_shift_right}\n'
      f'5 "Сдвиг влево на" 2 = {bit_shift_left}')
