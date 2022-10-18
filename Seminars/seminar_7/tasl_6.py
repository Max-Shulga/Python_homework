# 5. Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет, 
# можно ли из этих отрезков составить треугольник. 
# Входные данные
# Выходные данные
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)

def triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        print('треугольнику быть')
    else:
        print('нет')

print(triangle(7,6,10))

exit()
l = [i for i in range(10, 100)]
l1 = list(filter(lambda x: x % 9 == 0, l))
l2 = sum(list(map(lambda x: x**2, l1)))
print(l2)
