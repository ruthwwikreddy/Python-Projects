import random as rd

# declaring Ruthwik positions
j_position = ['L', 'M', 'R']


# main game function
def game():
    # taking player name
    playerName = input('\nPlease enter your name : ')

    # declaring default scores
    RuthwikScore = 0
    playerScore = 0

    print('\nPenalty Time!\nBest of luck :-)')

    # penalty taking
    for i in range(5):
        # taking choice of Ruthwik and player
        RuthwikChoice = rd.choice(j_position)
        playerChoice = input("\nType 'L' or 'l' for Left , 'M' or 'm' for Middle and 'R' or 'r' for Right : ")

        # comparing the choices
        # taking the case if Ruthwik stopped the penalty
        if playerChoice.upper() in j_position:
            if playerChoice.upper() == RuthwikChoice:
                print('\nRuthwik stopped the penalty!\n')
                # printing current scores
                print(f'Current Scores: \nPlayer Score = {playerScore} \nRuthwik Score = {RuthwikScore} ')

            # if Ruthwik didn't stopped then player scored
            else:
                print(f'\n{playerName} scored!\n')
                playerScore = playerScore + 1
                # printing current scores
                print(f'Current Scores: \nPlayer Score = {playerScore} \nRuthwik Score = {RuthwikScore} ')

            # printing choices of Ruthwik and player
            print(f'\nPlayer Chose = {playerChoice.upper()}\nRuthwik Chose = {RuthwikChoice}')

        # if player didn't choose between L, M or R
        else:
            print('You can only choose L, M or R')

    print('\nPenalty Saving Time!\nStop Ruthwik before he destroy you ;-)')

    # penalty saving
    for j in range(5):
        # taking choice of Ruthwik and player
        RuthwikChoice = rd.choice(j_position)
        playerChoice = input("\nType 'L' or 'l' for Left , 'M' or 'm' for Middle and 'R' or 'r' for Right : ")

        # comparing the choices
        # taking the case if j stopped the penalty
        if playerChoice.upper() in j_position:
            if playerChoice.upper() == RuthwiksChoice:
                print(f'\n{playerName} stopped the penalty!\n')
                # printing current scores
                print(f'Current Scores: \nPlayer Score = {playerScore} \nRuthwik Score = {RuthwikScore} ')

            # if player didn't stopped then Ruthwik scored
            else:
                print('\nRuthwik scored!\n')
                RuthwikScore = RuthwikScore + 1
                # printing current scores
                print(f'Current Scores: \nPlayer Score = {playerScore}\nRuthwik Score = {RuthwikScore} ')

            # printing choices of Ruthwik and player
            print(f'\nPlayer Chose = {playerChoice.upper()}\nRuthwik Chose = {RuthwikChoice}')

        # if player didn't choose between L, M or R
        else:
            print('You can only choose L, M or R')

    # DECLARING THE WINNER
    # if player won
    if playerScore > RuthwikScore:
        scoreDif = playerScore - RuthwikScore
        print(f'\n{playerName} won!\n')

        # a bit of commentry
        if scoreDif >= 3:
            print(f'{playerName} dominated Ruthwik!')
        elif scoreDif == 1:
            print(f'That was a very close match but there can be only one winner and that is {playerName}')
        else:
            print('That was a wonderful match!')

    # if Ruthwik won
    elif playerScore < RuthwikScore:
        scoreDif = RuthwikScore - playerScore
        print('\nRuthwik won!\n')

        # a bit of commentry
        if scoreDif >= 3:
            print(f'Ruthwik dominated {playerName}!')
        elif scoreDif == 1:
            print(f'That was a very close match but there can be only one winner and that is Ruthwik')
        else:
            print('That was a wonderful match!')

    # if match tied
    else:
        print('The match is tied!\nWonderful play by both Players')

    # asking the player if he/she wanna play again
    again = input("Wanna play again? Press 'y'or 'Y' to play again or press 'x' or 'X' to exit : ")
    if again.lower() == 'y':
        game()
    else:
        print('\nThanks for playing. Hoping to see you soon')

    # explaining the game rules to players


print(
    'Welcome to Penalty Kicker!\n\nGame rules:\nFirst you will take penalties then the pc will(pc character name is Ruthwik):\nBoth sides will take 5 Penalties\nYou can choose three position in both taking Penalties and Goal Keeping, That are Middle, Left and Right\nYou have to type \'L\' for Left, \'M\' for Middle and \'R\' for Right\nIf you will type anything rather than L, M or R your chance will be taken as well as score will not increase \nBest of Luck :-)\n')

# starting the game
start = input("Press 's'or 'S' to start game or press 'x' or 'X' to exit : ")

if start.lower() == 's':
    game()
else:
    print('Please come again :-)')
