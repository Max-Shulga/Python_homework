# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# -------------------------------------------------------------------------------------------------------------

x = int(input('enter the number of the day of the week: '))
if 0 >= x or x > 7:
    print('No day with this number')
elif x == 6 or x == 7:
    print('yes')
else:
    print('no')
