print('Введите длины 3-х отрезков (a,b,c):')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if (a + b) <= c or (a + c) <= b or (b + c) <= a:
    print("Треугольника с такими длинами сторон не существует")
elif a == b == c:
    print("Получается равносторонний треугольник")
elif a == b or a == c or b == c:
    print("Получается равнобедренный треугольник")
else:
    print("Получается разносторонний треугольник")
