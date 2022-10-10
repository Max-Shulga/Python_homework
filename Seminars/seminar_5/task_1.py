a=24
b=54

if a < b :
    a, b = b, a

while b!=0:
    a, b = b, a % b

print(a)

exit()




def find_simple(n):
    list_n = []
    for i in range(1,n):
        if n % i == 0:
            list_n.append(i)
            n / i
    return list_n

x = 24
y = 54
list_x = find_simple(x)
list_y = find_simple(y)

print(list_x)
print(list_y)

esult=list(set(list_x) & set(list_y))
print(max(esult))

exit()
# list_r = [i for i in list_x and list_y if list_a[i]. and count ]
# list_r = list_x + list_y

