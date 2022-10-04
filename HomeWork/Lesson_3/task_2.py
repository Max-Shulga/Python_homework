# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


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
