


pol_1 = '1*(x**2) + 1*x + 4 = 0'
pol_2 = '8*(x**2) + 4*x + 5 = 0'
pol_result = ''
for i in range(len(pol_1)):
    if  pol_1[i].isdigit() == True and pol_2[i].isdigit() == True:
        pol_result += str(int(pol_1[i]) + int(pol_2[i]))
    else:
        pol_result += pol_1[i]

print(pol_result)