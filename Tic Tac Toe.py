'''
TIC TAC TOE
PLAYER VS COMPUTER
'''

import random

player_1 = input("Enter player 1 name : ")
player_2 = 'James'
print(f'Player 2 name(pc) is {player_2}')
game = True
winner = "none"
count = 0
slots = [1,2,3,4,5,6,7,8,9]
mode = input('Which mode do you want to play in Easy, Medium or Hard(unbeatable) : ')

#assign characters "x or o"
player1_character = input(f"{player_1} what character do you want (x or o) : ")
if player1_character == "x":
    player2_character = "o"
else:
    player2_character = "x"
    player1_character = "o"


#who will go first
whoWillGoFirst = random.randint(1,2)

if whoWillGoFirst == 1:
    print(f"{player_1} will go first\n{player_2} will go second")
else:
    print(f"{player_2} will go first\n{player_1} will go second")


board = [" "," "," "," "," "," "," "," "," "," "]

#making the board
def board_game():
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

# making functions for player 1 turn and player 2
def player1_turn():
    position = int(input(f"{player_1} which position do you want to place your character (1 to 9)"))
    position = position - 1
    if board[position] == " ":
        board.pop(position)
        board.insert(position,player1_character)
        print("the board has been updated")
        board_game()
    else:
        print("the slot has been taken")
        player1_turn()

def ran():
    position = random.choice(slots)
    if board[position] == " ":
        board.pop(position)
        board.insert(position,player2_character)
        print("the board has been updated")
        board_game()
    else:
        ran()
    
        
#medium
def ai_turn_nor():
    position = 10
    stop = random.randint(1,2)
    if stop == 1:
        if board[0] == player1_character and board[1] == player1_character:
            position = 2
        elif board[1] == player1_character and board[2] == player1_character:
            position = 0
        elif board[0] == player1_character and board[2] == player1_character:
            position = 1
        elif board[3] == player1_character and board[4] == player1_character:
            position = 5
        elif board[4] == player1_character and board[5] == player1_character:
            position = 3
        elif board[3] == player1_character and board[5] == player1_character:
            position = 4
        elif board[6] == player1_character and board[7] == player1_character:
            position = 8
        elif board[7] == player1_character and board[8] == player1_character:
            position = 6
        elif board[6] == player1_character and board[8] == player1_character:
            position = 7
        elif board[0] == player1_character and board[4] == player1_character:
            position = 8
        elif board[4] == player1_character and board[8] == player1_character:
            position = 0
        elif board[0] == player1_character and board[8] == player1_character:
            position = 4
        elif board[2] == player1_character and board[4] == player1_character:
            position = 6
        elif board[4] == player1_character and board[6] == player1_character:
            position = 2
        elif board[2] == player1_character and board[6] == player1_character:
            position = 4
        elif board[0] == player1_character and board[3] == player1_character:
            position = 6
        elif board[3] == player1_character and board[6] == player1_character:
            position = 0
        elif board[0] == player1_character and board[6] == player1_character:
            position = 3
        elif board[1] == player1_character and board[4] == player1_character:
            position = 7
        elif board[4] == player1_character and board[7] == player1_character:
            position = 1
        elif board[1] == player1_character and board[7] == player1_character:
            position = 4
        elif board[2] == player1_character and board[5] == player1_character:
            position = 8
        elif board[5] == player1_character and board[8] == player1_character:
            position = 2
        elif board[2] == player1_character and board[8] == player1_character:
            position = 5
        else:
            ai_turn_sim()
        if position != 10:
            if board[position] == " ":
                board.pop(position)
                board.insert(position,player2_character)
                print("the board has been updated")
                board_game()
            else:
                ran()
    if stop == 2:
        ai_turn_sim()

#hard
def ai_turn_hard():
    position = 10
    if board[0] == player2_character and board[1] == player2_character:
        position = 2
    elif board[1] == player2_character and board[2] == player2_character:
        position = 0
    elif board[0] == player2_character and board[2] == player2_character:
        position = 1
    elif board[3] == player2_character and board[4] == player2_character:
        position = 5
    elif board[4] == player2_character and board[5] == player2_character:
        position = 3
    elif board[3] == player2_character and board[5] == player2_character:
        position = 4
    elif board[6] == player2_character and board[7] == player2_character:
        position = 8
    elif board[7] == player2_character and board[8] == player2_character:
        position = 6
    elif board[6] == player2_character and board[8] == player2_character:
        position = 7
    elif board[0] == player2_character and board[4] == player2_character:
        position = 8
    elif board[4] == player2_character and board[8] == player2_character:
        position = 0
    elif board[0] == player2_character and board[8] == player2_character:
        position = 4
    elif board[2] == player2_character and board[4] == player2_character:
        position = 6
    elif board[4] == player2_character and board[6] == player2_character:
        position = 2
    elif board[2] == player2_character and board[6] == player2_character:
        position = 4
    elif board[0] == player2_character and board[3] == player2_character:
        position = 6
    elif board[3] == player2_character and board[6] == player2_character:
        position = 0
    elif board[0] == player2_character and board[6] == player2_character:
        position = 3
    elif board[1] == player2_character and board[4] == player2_character:
        position = 7
    elif board[4] == player2_character and board[7] == player2_character:
        position = 1
    elif board[1] == player2_character and board[7] == player2_character:
        position = 4
    elif board[2] == player2_character and board[5] == player2_character:
        position = 8
    elif board[5] == player2_character and board[8] == player2_character:
        position = 2
    elif board[2] == player2_character and board[8] == player2_character:
        position = 5
    else:
        ai_turns_hard()

    if position != 10:
        if board[position] == " ":
            board.pop(position)
            board.insert(position,player2_character)
            print("the board has been updated")
            board_game()
        else:
            ai_turns_hard()

def ai_turns_hard():
    position = 10
    if board[0] == player1_character and board[1] == player1_character:
        position = 2
    elif board[1] == player1_character and board[2] == player1_character:
        position = 0
    elif board[0] == player1_character and board[2] == player1_character:
        position = 1
    elif board[3] == player1_character and board[4] == player1_character:
        position = 5
    elif board[4] == player1_character and board[5] == player1_character:
        position = 3
    elif board[3] == player1_character and board[5] == player1_character:
        position = 4
    elif board[6] == player1_character and board[7] == player1_character:
        position = 8
    elif board[7] == player1_character and board[8] == player1_character:
        position = 6
    elif board[6] == player1_character and board[8] == player1_character:
        position = 7
    elif board[0] == player1_character and board[4] == player1_character:
        position = 8
    elif board[4] == player1_character and board[8] == player1_character:
        position = 0
    elif board[0] == player1_character and board[8] == player1_character:
        position = 4
    elif board[2] == player1_character and board[4] == player1_character:
        position = 6
    elif board[4] == player1_character and board[6] == player1_character:
        position = 2
    elif board[2] == player1_character and board[6] == player1_character:
        position = 4
    elif board[0] == player1_character and board[3] == player1_character:
        position = 6
    elif board[3] == player1_character and board[6] == player1_character:
        position = 0
    elif board[0] == player1_character and board[6] == player1_character:
        position = 3
    elif board[1] == player1_character and board[4] == player1_character:
        position = 7
    elif board[4] == player1_character and board[7] == player1_character:
        position = 1
    elif board[1] == player1_character and board[7] == player1_character:
        position = 4
    elif board[2] == player1_character and board[5] == player1_character:
        position = 8
    elif board[5] == player1_character and board[8] == player1_character:
        position = 2
    elif board[2] == player1_character and board[8] == player1_character:
        position = 5
    else:
        ran()

    if position != 10:
        if board[position] == " ":
            board.pop(position)
            board.insert(position,player2_character)
            print("the board has been updated")
            board_game()
        else:
            ran()

#making function that will check winner
def winnerCheck():
    global game
    global winner
    global count
    if (board[0] == "x" and board[1] == "x" and board[2] == "x"
    or
    board[3] == "x" and board[4] == "x" and board[5] == "x"
    or
    board[6] == "x" and board[7] == "x" and board[8] == "x"
    or
    board[0] == "x" and board[4] == "x" and board[8] == "x"
    or
    board[2] == "x" and board[4] == "x" and board[6] == "x"
    or
    board[0] == "x" and board[3] == "x" and board[6] == "x"
    or
    board[1] == "x" and board[4] == "x" and board[7] == "x"
    or
    board[2] == "x" and board[5] == "x" and board[8] == "x"):
        if player1_character == "x":
            print(f"\n{player_1} wins the match")
            game = False
        else:
            print(f"\n{player_2} wins the match")
            game = False
    elif (board[0] == "o" and board[1] == "o" and board[2] == "o"
    or
    board[3] == "o" and board[4] == "o" and board[5] == "o"
    or
    board[6] == "o" and board[7] == "o" and board[8] == "o"
    or
    board[0] == "o" and board[4] == "o" and board[8] == "o"
    or
    board[2] == "o" and board[4] == "o" and board[6] == "o"
    or
    board[0] == "o" and board[3] == "o" and board[6] == "o"
    or
    board[1] == "o" and board[4] == "o" and board[7] == "o"
    or
    board[2] == "o" and board[5] == "o" and board[8] == "o"):
        if player1_character == "o":
            print(f"\n{player_1} wins the match")
            game = False
        else:
            print(f"\n{player_2} wins the match")
            game = False
    else:
        if count == 9:
            print("tie")
            game = False
    return game

#main game

if mode.lower() == 'easy':
    while game == True:
        if whoWillGoFirst == 1:
            player1_turn()
            count = count + 1
            winner_check = winnerCheck()
            if winner_check == False:
                break
            ran()
            count = count + 1
            winner_check = winnerCheck()
            if winner_check == False:
                break
        else:
            ran()
            count = count + 1
            winner_check = winnerCheck()
            if winner_check == False:
                break
            player1_turn()
            count = count + 1
            winner_check = winnerCheck()
            if winner_check == False:
                break

if mode.lower() == 'medium':
    while game == True:
        if whoWillGoFirst == 1:
            player1_turn()
            count = count + 1
            winner_check = winnerCheck()
            if winner_check == False:
                break
            ai_turn_nor()
            count = count + 1
            winner_check = winnerCheck()
            if winner_check == False:
                break
        else:
            ai_turn_nor()
            count = count + 1
            winner_check = winnerCheck()
            if winner_check == False:
                break
            player1_turn()
            count = count + 1
            winner_check = winnerCheck()
            if winner_check == False:
                break


if mode.lower() == 'hard':
    print(whoWillGoFirst)
    while game == True:
        if whoWillGoFirst == 1:
            player1_turn()
            count = count + 1
            winner_check = winnerCheck()
            if winner_check == False:
                break
            ai_turn_hard()
            count = count + 1
            winner_check = winnerCheck()
            if winner_check == False:
                break
        else:
            ai_turn_hard()
            count = count + 1
            winner_check = winnerCheck()
            if winner_check == False:
                break
            player1_turn()
            count = count + 1
            winner_check = winnerCheck()
            if winner_check == False:
                break
