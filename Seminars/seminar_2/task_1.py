# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.


x = int(input('введите число: '))
count = 0
array = []
a = 1
print(type(array))
while count < x:
    array.append(a) 
    a = a* (-3)
    count += 1

print (f'{x} = {array}')











# n = int(input('введите число: '))
# for i in range(0,n):
#     print(-3**i,end = " ")