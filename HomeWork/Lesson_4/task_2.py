# Задайте натуральное число N. Напишите программу, которая составит список простых множителей ч
# Попробуем перечислить все простые числа от 1 до 10: 3, 5, 7.

numb = int(input('input number: '))
simple_numbers_list = [2, 3, 5, 7]
simple_numbers_list = simple_numbers_list + [i for i in range(7, numb+1, 2) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0]
simple_numbers_list.reverse()
result_list = []
for i in simple_numbers_list:
    while numb % i == 0:
        numb = numb/i
        result_list.append(i)
print(simple_numbers_list)
print(f'list of prime factors of number {numb} : {result_list}')

# result_list = [i for i in simple_numbers_list if numb % i == 0] работает но работает не совсем верно

# n = int(input("Введите число N: "))
# i = 2 
# list = []

# while i <= n:
#     if n % i == 0:
#         list.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители введенного числа указаны в списке: {list}")

