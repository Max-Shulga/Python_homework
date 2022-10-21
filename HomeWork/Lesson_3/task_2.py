# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random
b = int(input('Введите кол-во чисел в списке for 2# = '))
list_b = list(random.randint(0, 10) for i in range(b))
print(list_b)
proiz_b = list(list_b[i]*list_b[-1*(1+i)] for i in range(b//2+1*(b%2)))
print(proiz_b)

exit()

import math

array = [2, 3, 4, 5, 6]
prod = 1
prod_array = list((int(array[i] * array[len(array)-i-1])) for i in range(math.ceil(len(array)/2)))
print(prod_array)


def elements_sum(array=[], result_array: list = []):
    if len(array) >= 2:
        result_array.append(array[0] * array[-1])
        return elements_sum(array[1:-1], result_array)
    else:
        if len(array) == 1:
            result_array.append(array[0] **2 )
        return result_array

numbers_list = list(map(int, input('Enter a list of numbers separated by a space: ').split()))
print(f'{numbers_list} => {elements_sum(numbers_list)}')
