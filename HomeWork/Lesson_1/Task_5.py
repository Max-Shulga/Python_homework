#  Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#  Пример:

#  - A (3,6); B (2,1) -> 5,09
#  - A (7,-5); B (1,-1) -> 7,21

from math import sqrt


def dist_points(a1, b1, a2, b2):
    d = ((a2 - a1)**2 + (b2-b1)**2) ** 0.5
    d = round(d, 2)
    return d


def dist_points2(a1, b1, a2, b2):
    d = sqrt(pow((a2 - a1), 2) + pow((b2-b1), 2))
    d = round(d, 2)
    return d


x1 = float(input('enter the X coordinates of the first point: '))
y1 = float(input('enter the Y coordinates of the first point: '))
x2 = float(input('enter the X coordinates of the second point: '))
y2 = float(input('enter the Y coordinates of the second point: '))
print(f'A{x1,y1}; B{x2,y2} -> {dist_points(x1,y1,x2,y2)}')
print(f'A{x1,y1}; B{x2,y2} -> {dist_points2(x1,y1,x2,y2)}')
