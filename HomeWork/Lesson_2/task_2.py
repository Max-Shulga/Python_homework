# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Комменатрий: пытаюсь понять рекурсию, но пока она понимает меня лучше чем я её, мне все это выглдит как костыли.
# Буду благодарен если дадите совет как это можно было бы улучшить

list = []


def factorial_list(n):
    if n >= 1:
        result = 1
        i = 1
        for i in range(i, n):
            result += result * i
        list.append(result)
        return factorial_list(n-1)
    else:
        list.reverse()
        return list


print(f"{'-' * 100}\n START\n")
n = int(input('input number: '))
print(f'{n}! mass = {factorial_list(n)}')
print(f"\n END \n {'-' * 100}")
