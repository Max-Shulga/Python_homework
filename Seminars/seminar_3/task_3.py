# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

list = ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen','an123ton', 'aoooooooooontooooo']
num =123


for word in list:
    if str(num) in word:
        print(True)
    else:
        print(False)
    