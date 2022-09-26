# ; **Задачи:**

# ; 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
# ;     *Примеры:* 
    
# ;     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


n = int(input('Input number: '))

for i in range(-n,n+1):
    print(i, end = " ")

# num = -n
# while (num <= n):
#     print(num, end = " ")
#     num += 1

# print('введите числа')

# value = int(input())

# print (list (range(-value, value+1)))


