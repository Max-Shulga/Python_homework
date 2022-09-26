# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

num_1 = int(input('input first number: '))
num_2 = int(input('input second number: '))

if num_1 == num_2*num_2 or num_2 == num_1*num_1:
    print('yes')
else:
    print('no')