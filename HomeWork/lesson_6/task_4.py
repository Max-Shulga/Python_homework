# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


numbers = [2, 3, 4, 5, 6, 7, 5]
diff = list([a*b for a, b in zip(numbers, numbers[:(len(numbers)//2) - 1: -1])])
print(diff)


exit()
numb_list = list(map(int, input('input numbers: ').split()))
list = [i for i in numb_list if numb_list.count(i) == 1]
print(list)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

# import random
# list3 = [random.randint(0,10) for i in range(random.randint(5,10))]
# result_list = list(filter(lambda a: list3.count(a) == 1, list3))
# print(f'Для последовательности\n{list3}\n   список уникальных элементов\n{result_list}')

