# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def check_index(array,x):
    if array.index(x)%2 != 0:
        return True
    else:
        return False

abc =  list(map(int, input('input numbers list: ').split()))
print(sum(filter(lambda x: check_index(abc,x), abc)))