# ; Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# -------------------------------------------------------------------------------------------------------------

plate = {1: 'x > 0; y > 0',
         2: 'x < 0; y > 0',
         3: 'x < 0; y < 0',
         4: 'x > 0; y < 0'}

plates_numb = int(input('enter plane number: '))
if 0 < plates_numb < 5: 
    print(plate[plates_numb])
else:
    print('incorrect value')

