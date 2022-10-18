# Создайте программу для игры в ""Крестики-нолики"".

# в коде есть несколько моментов которые я бы покрасивее переделал, но сроки сдачи горят))
from random import randint as ri


def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")


def win_combination(list):
    one = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
           [3, 6, 9], [2, 5, 8], [1, 5, 9], [3, 5, 7]]
    count = 0
    for i in one:
        for n in i:
            for k in list:
                if n == k:
                    count += 1
            if count >= 3:
                return True
        count = 0


def corrective_input():
    place = int(input(f'{player_2} where do you want to place the сircle: '))
    while place <= 0 or place > 9:
        place = int(input('invalid input, please try again: '))
    while str(board[place - 1]) in 'XO':
        place = int(input('this square is already occupied, choose another: '))
        while place <= 0 or place > 9:
            place = int(input('invalid input, please try again: '))
    return place


board = [i for i in range(1, 10)]
player_1 = input('input player 1 name: ').capitalize()
player_2 = input('input player 2 name: ').capitalize()

lottery = ri(0, 1)
if lottery == 1:
    print(f'{player_1} take the first move.')
else:
    print(f'{player_2} take the first move.')
step = 1
list_one = []
list_two = []
list_winner = []
while step <= 9:
    draw_board(board)
    if win_combination(list_winner) == True:
        print(f'Congratulation {winner}, you WIN')
        break
    else:
        if lottery == 1:
            sign = corrective_input()
            list_one.append(sign)
            list_winner = list_one
            winner = player_1
            lottery = 0
            board[sign - 1] = 'X'
        else:
            sign = corrective_input()
            list_two.append(sign)
            list_winner = list_two
            winner = player_2
            lottery = 1
            board[sign - 1] = 'O'
    step += 1
