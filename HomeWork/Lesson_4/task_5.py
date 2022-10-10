import random


def take_polynomial():
    file = open('file_2.txt', 'r')
    line_number = random.randint(0, sum(1 for line in file))
    string = str([i for line,  i in enumerate(
        open('file_1.txt', 'r+')) if line == line_number-1][0]).strip()
    # 22 полный, 11 без квадрата,  18 без  простого числа
    return string

pol_1 = take_polynomial()
pol_2 = take_polynomial()
pol_result = ''
for i in range(len(pol_1)):
    if pol_1[i].isdigit() == True and pol_2[i].isdigit() == True:
        pol_result += str(int(pol_1[i]) + int(pol_2[i]))
    else:
        pol_result += pol_1[i]

file = open('file_3.txt', 'w')
file.write(pol_result)
file.close