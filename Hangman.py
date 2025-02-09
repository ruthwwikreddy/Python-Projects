def get_player_name():
    player_name = input('Enter your name: ')
    return player_name
    
player_name = get_player_name()
print('Hello',player_name,',Lets Play Hangman!')

words_possible = {'secret':['_','_','c','_' ,'_','t'],'game':['_', '_', 'm', '_'],'dragon':['_','r','_','_','_','n'],'python':['_','_','t','_','o','_'],'interpreter':['_','_','_','e','_','p','_','_','t','_','r',]}
    
import random
word = random.choice(list(words_possible.keys()))
word_to_print = words_possible[word]
print(word_to_print)


chances=5
while chances>0:
    guess = input('Enter a character: ')
    
    if guess in word:
        print('Correct Guess')
        for i in range(len(word)):
            if word[i] == guess:
                word_to_print[i]=guess
        print(word_to_print)
        if '_' not in word_to_print:
            print('You Won!!')
            break
    else:
        chances = chances - 1 
        print('Wrong Guess')
        print('Chances left: ',chances)
   
    if chances == 0:
        print('Sorry you lost!!')
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |    /|\ \n"
            "  |    / \ \n"
            "__|__\n")    
    elif chances == 1:
        
        print("  _____ \n"
          "  |     | \n"
          "  |     |\n"
          "  |     | \n"
          "  |     O \n"
          "  |     \n"
          "  |     \n"
          "__|__\n")
          
    elif chances == 2:
        
        print("  _____ \n"
          "  |     | \n"
          "  |     |\n"
          "  |     | \n"
          "  |      \n"
          "  |     \n"
          "  |     \n"
          "__|__\n")
          
    elif chances == 3:
        
        print("  _____ \n"
          "  |     | \n"
          "  |     |\n"
          "  |      \n"
          "  |      \n"
          "  |     \n"
          "  |     \n"
          "__|__\n")
          
    elif chances == 4:
        
        print("  _____ \n"
          "  |     | \n"
          "  |     \n"
          "  |      \n"
          "  |      \n"
          "  |     \n"
          "  |     \n"
          "__|__\n")
