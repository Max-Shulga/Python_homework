# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def get_fractional_value(list):
    array = []
    for i in range(len(numbers_list)):
        temp_list = numbers_list[i].rsplit('.', 1)
        if len(temp_list) > 1:
            array.append(temp_list[1])
    for i in range(len(array)):
        if len(array[i]) == 1:
            array[i] = array[i] + '0'
    return array


numbers_list = input('Enter a list of numbers separated by a space: ').split()
fract_value_list = get_fractional_value(numbers_list)
print(f'{max(fract_value_list)} - {min(fract_value_list)} = 0.{int(max(fract_value_list)) - int(min(fract_value_list))}')
