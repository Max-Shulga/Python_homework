# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def elements_sum(array=[], sum=0,):
    if len(array) > 1:
        return sum + array[1] + elements_sum(array[2:], sum)
    else:
        return sum


numbers_list = list(map(int, input('Enter a list of numbers separated by a space: ').split()))
print(f'\n The sum of the elements in the odd position is: {elements_sum(numbers_list)}')
