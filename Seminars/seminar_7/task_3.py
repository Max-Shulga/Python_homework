# 3)На вход программы поступает список наименований рек, записанных в одну строчку через пробел.
#  Необходимо отсортировать этот список в порядке убывания длин названий. Результат вывести в одну строчку через пробел.

# Sample Input:
# Лена Енисей Волга Дон
# Sample Output:
# Енисей Волга Лена Дон

rivers = ['Лена', 'Енисей', 'Волга', 'Дон']
x = rivers.sort(key=lambda x: len(x), reverse=True)
print(rivers)

exit()
s=sorted(input().split(), key=lambda x: len(x))[::-1]
print(*s)
#не меняет первоисточник