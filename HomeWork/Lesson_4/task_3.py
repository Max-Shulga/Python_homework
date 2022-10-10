# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numb_list = list(map(int, input('input numbers: ').split()))
list = [i for i in numb_list if numb_list.count(i) == 1], 
print(list)

