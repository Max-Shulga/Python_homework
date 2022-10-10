aplphE = ['a', 'b', 'v', 'g', 'd', 'e', 'yo', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p','r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '\'', 'e', 'yu', 'ya']

aplphR = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

base = input('Введите слово: ')

for i in range(len(base)):
    print(base[i].replace(aplphR[aplphR.index(base[i])],aplphE[aplphR.index(base[i])]), end = '')
    
exit()
t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

start_index = ord('а')
title = 'Переводим этот текст, сейчас!'
print(title.lower())

slug = ""
for s in title.lower():

	if "а" <= s <= "я":
		slug += t[ord(s) - ord('а')]
	
	else:
		slug += s



print(slug)

# base_tr = ''
# for i in range(len(base)):
#     print(base[i].replace(aplphR[aplphR.index(base[i])],aplphE[aplphR.index(base[i])]), end = '')
#     base_tr += base[i].replace(aplphR[aplphR.index(base[i])],aplphE[aplphR.index(base[i])])
# print (base_tr)



# for i in range(len(base)):
#     word.append(aplphR.index(base[i]))
#     index = word[i]
#     print(aplphE[index], end='')


# transleterate = \
#   {'а': 'a','б': 'b','в': 'v','г' : 'g','д' : 'd','е' : 'e','ж' : 'zh','з' : 'z','и' : 'i',
#   'й' : 'y','к' : 'k','л' : 'l','м' : 'm','н' : 'n','о' :'o','п' : 'p','р' : 'r','с' : 's',
#   'т' : 't','у' : 'u','ф' : 'f','х' : 'kh','ц' : 'ts','ч' : 'ch','ш' : 'sh','щ' : 'shch',
#   'ь' : '\'','ы' :'y','ъ' : '','э' : 'e','ю' : 'yu','я' : 'ya'}
# text = input('input: ')

# for i in text:
#     print(transleterate[i], end = "")
