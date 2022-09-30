# Задайте список из n чисел последовательности (1 + 1 / n) ** n  и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


def get_number_list(x):
    num_list = []
    for i in range(1, n+1):
        num_list.append(round(((1+1/i)**i), 3))
    return num_list



print(f"{'-' * 100}\n START\n")
n = int(input('input number: '))
print(get_number_list(n))
print(f"\n END \n {'-' * 100}")
