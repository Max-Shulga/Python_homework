# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# Коментарий: можно было и с приемом float, через if проверять больше или меньше 0, есть ли знаки после '.'
# и потом % или /10 сумировать числа но мы так 100 раз делали пока C# разбирали, поэтому я сделал извращение.

# def del_not_num(text):
#     for i in range(len(text)):
#         if text[i].isdigit() == False:
#             text = text[:i] + " " + text[i+1:]
#     text = text.replace(" ", "")
#     text = ' + '.join(text)
#     return text


# def sum_element(text):
#     count = 0
#     for i in range(len(text)):
#         if text[i].isdigit() == True:
#             count += int(text[i])
#     return count


# print(f"{'-' * 100}\n START\n")
# a = input('Input number: ')
# print(f'Sum of element: {a} = {del_not_num(a)} = {sum_element(a)}')
# print(f"\n END \n {'-' * 100}")

print(sum([int(i) for i in input('input some number: ') if i.isdigit()]))
