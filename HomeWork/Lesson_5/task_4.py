# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

# как то криво:( мне не нравится

numbers = [7, 7, 7, 7, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
set_index = [i for i in set(numbers)]

rle_list = []

for i in set_index:
    rle_list.append((numbers.count(i), i))
# я пока что сдаюсь как это в одну строчку красиво записать
new_list = []
print(rle_list)
for i in rle_list:
    x = i[0]
    while x >= 0:
        new_list.append(i[1])
        x -= 1

print(new_list)
