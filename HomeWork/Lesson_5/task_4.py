# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

# как то криво:( мне не нравится

text = input('Введите строку: ')

def Squash(inp_text):
    result = []
    i=0
    while i in range(len(inp_text) - 1):
        counter = 1
        key = inp_text[i]
        for j in range(i + 1, len(inp_text)):
            if key == inp_text[j]:
                counter += 1
            else:
                i += counter
                if counter == 1:
                    result.append((key, 1))
                else:
                    result.append((key, counter))
                break
    result.append((inp_text[-1], 1))
    return result

def Unpack (inp_list):
    result=''
    for i in inp_list:
        result = result + i[0]*i[1]
    return result

a = Squash(text)
print(a)
print (Unpack(a))



exit()
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
