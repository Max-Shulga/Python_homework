numbers = [7,7,7,7,2,2,2,2,3,3,3,4,4,4,5,5,5]
set_index = [i for i in set(numbers)]

x = [[j for j in numbers] for i in set_index]
print(x)