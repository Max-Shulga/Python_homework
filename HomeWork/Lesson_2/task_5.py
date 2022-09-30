# Реализуйте алгоритм перемешивания списка
import random

def mix_list(list):
    for i in range(len(massive)):
        random_int_1 = random.randint(0, len(massive)-1)
        random_int_2 = random.randint(0, len(massive)-1)
        massive[random_int_1],massive[random_int_2] = massive[random_int_2],massive[random_int_1]
    return massive

massive = input("Input the list element separated by a space: ").split()
print(massive)
# random.shuffle(massive)
# print (massive)
# Как - то слишком просто. 
massive_2 = mix_list(massive)
print(massive_2)