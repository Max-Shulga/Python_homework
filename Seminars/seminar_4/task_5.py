import random


def take_polynomial():
    file = open('file_1.txt', 'r')
    line_number = random.randint(0, sum(1 for line in file))
    string = str([i for line,  i in enumerate(open('file_1.txt', 'r+')) if line == line_number-1][0]).strip()
    string = '.'.join(string).split('.') #22 полный, 11 без квадрата,  18 без  простого числа
    return string



pol_1 = '1*(x**2) + 1*x + 4 = 0'
#22 полный, 11 без квадрата,  18 без  простого числа
pol_2 = '2*x + 2 = 0'
pol_2 = pol_2.rjust(22, '0')
pol_type = {22: 1, 11: 2, 18: 3}
print(pol_2)
len_pol_1 = len(pol_1)
len_pol_2 = len(pol_2)
pol_2 = str(pol_2,)
print(pol_2.replace("'", '').replace(",", '').replace(' ', ''))
#как сумировать 1 и 1
