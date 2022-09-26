# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 9

# num_1 = int(input('input first number: '))
# num_2 = int(input('input second number: '))
# num_3 = int(input('input third number: '))
# num_4 = int(input('input fourth number: '))
# num_5 = int(input('input fifth number: '))

# max_num = num_1

# if num_2 > max_num:
#     max_num = num_2
# elif num_3 > max_num:
#     max_num = num_3
# elif num_4 > max_num:
#     max_num = num_4
# elif num_5 > max_num:
#     max_num = num_5

# print(f'max num is {max_num}')

numbers = int(input(' input amount of numbers:  '))
count = 1
arr = []
while( count <= numbers):
    num = int(input(f"input {count} number: "))
    arr.append(num)
    count += 1 
print (arr)
max_num = arr[0]
for i in arr:
    if i > max_num:
        max_num = i

print(f' max number is: {max_num}')

    