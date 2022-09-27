# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1

# -------------------------------------------------------------------------------------------------------------

def try_to_int(x):
    if (x*10) % 10 == 0:
        x = int(x)
    return x


def find_plate(x, y):
    if x > 0 and y > 0:
        plate = 1
    elif x < 0 and y > 0:
        plate = 2
    elif x < 0 and y < 0:
        plate = 3
    elif x > 0 and y < 0:
        plate = 4
    else:
        print('incorrect value')
    return plate

x = float(input('input x value: '))
y = float(input('input y value: '))

x = try_to_int(x)
y = try_to_int(y)
plate = find_plate(x,y)

print(f'x={x}; y={y} -> {plate}')
