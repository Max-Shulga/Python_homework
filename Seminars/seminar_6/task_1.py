# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
# отдельно буквы и цифры.
numb_list = list(map(int, input('input numbers: ').split()))

result = list(filter(lambda x: len(str(abs(int(x)))) == 2,numb_list))
print(result)

# x = lambda x: for i in numb_list
# result = filter(check(x),numb_list)
# print(result)