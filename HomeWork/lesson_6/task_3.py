# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

print(list(filter(lambda x: 'abc' not in x, input('input some text: ').split())))

