# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input('input number: '))
file = open('file_1.txt', 'w')
arrays = random.randint(0, 101)
for i in range(arrays):
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)
    num_3 = random.randint(0, 9)

    if num_1 == 0 or num_2 == 0 and num_3 != 0:
        if num_2 == 0 and num_1 == 0:
            continue
        elif num_1 == 0:
            file.write(f'{num_2}*x + {num_3} = 0\n')
        elif num_2 == 0:
            file.write(f'{num_1}*(x**{k}) + {num_3} = 0\n')
        else: continue
    elif num_3 == 0:
        if num_1 == 0:
            file.write(f'{num_2}*x= 0\n')
        elif num_2 == 0:
            file.write(f'{num_1}*(x**{k})= 0\n')
        else:
            file.write(
                f'{num_1}*(x**{k}) + {num_2}*x = 0\n')
    else:
        file.write(
            f'{num_1}*(x**{k}) + {num_2}*x + {num_3} = 0\n')
file.close()

