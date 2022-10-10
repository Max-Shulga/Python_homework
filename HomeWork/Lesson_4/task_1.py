# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi


def round(x=pi, d=3):
    x = float(str(x)[:str(x).find('.')+(d + 1)])
    return x


print(round())
