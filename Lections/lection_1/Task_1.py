list = [1, 2, 3, 5, 8, 15, 23, 38]
res = lambda a : a**2
list_2 = [(i,res(i)) for i in list if i %2 !=0]
print(list_2)