# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint as ri


def bot_ligiq(candy, limit):
    number = 1
    if candy > limit + limit + 1:
        if candy % (limit + 1) != 0:
            for number in range(0, limit):
                if (candy - number) % (limit+1) == 0:
                    break
            return number
    elif candy > limit:
        number = candy - (limit + 1)
    else:
        number = candy
    if number == 0:
        number = 1
    return number


def limitation(candy, limit):
    while candy > limit or candy <= 0:
        candy = int(
            input('you want to take too much, or to lees candies try again: '))
    return candy


candy = 200
limit = 28
player_1 = input('Input your nickname: ').capitalize()
player_2 = 'bot_Andrey'
lottery = ri(0, 1)
if lottery == 1:
    print(f'{player_1} take the first move.')
else:
    print(f'{player_2} take the first move.')
print('Game Start!')
while candy > 0:
    print(f'{candy} candys left on the tab.')
    if lottery == 1:
        candy -= limitation(
            int(input(f'{player_1} how many candies would you like to take?: ')), limit)
        lottery = 0
        winner = player_1
    else:
        print(f'{player_2} take {bot_ligiq(candy, limit)} candies.')
        candy -= bot_ligiq(candy,limit)
        lottery = 1
        winner = player_2
if candy == 0:
    print(f'\nEnd. Winner is: {winner}.')
