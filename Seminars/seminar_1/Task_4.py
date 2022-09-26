# ; 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
# ;     *Примеры:*
    
# ;     - 6,78 -> 7
# ;     - 5 -> нет
# ;     - 0,34 -> 3

# import math

# number = float(input('input float number: '))
# num_result = number*10

# if num_result%10 == 0:
#     print('none')
# else:
#     print(math.floor(num_result)%10)

f = float(input())
d = int( (f*10) % 10 )
print(f, d, sep=" -> ")
