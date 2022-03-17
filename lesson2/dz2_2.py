number = input('Введите любое натуральное число: ')

even = 0
even_list = []
odd = 0
odd_list = []
numbers = [int(num) for num in number]
for num in numbers:
    if num % 2 == 0:
        even += 1
        even_list.append(num)
    else:
        odd += 1
        odd_list.append(num)
even_str = ','.join([str(i) for i in even_list])
odd_str = ','.join([str(n) for n in odd_list])
print(f'У вашего числа {even} четные цифры ({even_str}) и {odd} нечетные ({odd_str})')
