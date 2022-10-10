# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# num = int(input("Введите число: "))
# binum = ''

# while num:
#     binum = str(num%2) + binum
#     num //= 2

# print(binum)

a = int(input('введите число для перевода = '))
b = ''
while a != 0:
    b = str(a % 2) + b
    a = a // 2
print(b)

exit()
def to_binar(number, array: list = []):
    number = int(number)
    if number == 0:
        array.append(0)
        return array
    if number == 1:
        array.append(1)
        array.reverse()
        return array
    if number % 2 == 0:
        array.append(0)
        return to_binar(number/2, array)
    else:
        array.append(1)
        return to_binar((number-1)/2, array)

number = int(input('input number: '))
print(f'your number ({number}) in binary system = {to_binar(number)}')
