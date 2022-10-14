# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

print(' '.join(str(i) for i in([i for i in input('input some text: ').split() if 'abc' not in i])))
