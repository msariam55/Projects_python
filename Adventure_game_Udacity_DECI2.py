# using libraries (time,random)
import time 
import random
# use random to do random colors
colors=random.choice([ "\033[31m" # red, 
                "\033[32m" ,#green 
                "\033[33m",# yellow 
                "\033[34m", # blue
                "\033[35m",# megenta
                "\033[36m",# cyan
                "\033[37m",# white
                "\033[0m" ])# reset
Score=0# variable to calculate points
def sleep_print (msg,color=colors):# sleep for specifid secound time to run text
    time.sleep(2) 
    print(msg,color)
 # to take extra points in game
def increase_points():
    global Score
    while True:
        # ask player if he wants to take extra points or no
        player=input('\nWould you like to add extra points in your score? you will be  ask some questions.'+'\n'+'Enter your choice(yes or no): ').lower()
        if player=='yes':
            while True:
                sleep_print('Q1-When was the sixth of the October war?'+'\n'+' 1-1952\n 2-1972\n 3-1977')
                ans1=int(input('Enter your answer: '))
                if ans1 == 1972:
                    sleep_print('valid answer')
                    Score+=10
                    break 
                if ans1 in [1952,1977]:
                    sleep_print('invalid answer')
                    Score-=5 
                    break
                if ans1 not in [1972,1952,1977]:
                    print('invalid input ',0)  
            break      
        elif player=='no':
            sleep_print('you lose your chance') 
            break  
        elif player is not['yes','no']:
            print('invalid input',0)
        print(f'your score :{Score}')    
        
        
def again_Game():# to play the game again
    choice3_player=input('Would you like to play again? Enter your choice (yes or no): ').lower()
    if choice3_player=='yes':
        start_game()
    elif choice3_player=='no':
        print('You lose your chance')
    elif choice3_player is not ['yes','no']:
         again_Game() 
          
# to choose right path
def right_path():
    global Score
    sleep_print('\nYou come across a beautiful meadow filled with flowers.')
    sleep_print('\nYou bask in the peaceful surroundings for a while before continuing on your journey. ')
    sleep_print('\nAs you walk, you see a group of goblins up ahead.')
    sleep_print('\nWhat would you like to do?')
    sleep_print('\n1-Try to reason with the goblins'+'\n'+'2-Fight the goblins ')
    while True:
        choice_player2=input('Enter your choice: (1 or 2): ')# choosw try to reason with goblins
        if choice_player2=='1':
            sleep_print('\nYou approach the goblins and try to reason with them. ')
            sleep_print('\nThey listen to what you have to say and ultimately decide to let you pass unharmed.')
            Score+=10
            sleep_print('you won')
            sleep_print(f'your Score: {Score}')
            break
        if choice_player2=='2':# choose fight goblins
            sleep_print('\nYou engage in a battle with the goblins.')
            sleep_print('\nAfter a tough fight, you manage to defeat them and continue on your way.')
            Score+=5
            print('you won in the game but there are another ways to take alot of points in game')
            sleep_print(f'your Score: {Score}')
            increase_points()
            break
        elif choice_player2 is not ['1','2']:
            print('invalid choice',0)
            
# to choose left path                
def left_path():
    global Score
    sleep_print('\nYou come across a chest filled with gold.')
    sleep_print('\nYou take the gold and continue on your way.')
    sleep_print('\nAs you walk, you see a troll up ahead.')
    sleep_print('\nWhat would you like to do?')
    sleep_print('\n1-Fight the troll '+'\n'+'\n2-Try to sneak past the troll') 
    while True:
        choice_player2=input('Enter your choice:(1 or 2): ')# choose fight the troll
        if choice_player2=='1':
            sleep_print('\nYou engage in a fierce battle with the troll. ')
            sleep_print('\nAfter a hard-fought struggle, you emerge victorious.')
            Score+=10
            sleep_print('\nyou won')
            sleep_print(f'your score: {Score}')
            increase_points()
            break
        if choice_player2=='2':# choose try to sneak past the troll
            sleep_print('\nYou try to sneak past the troll, but it catches sight of you and gives chase.')
            sleep_print('\nYou run as fast as you can, but the troll eventually catches up and defeats you.')
            Score-=10
            sleep_print('you lose game')
            sleep_print(f'your score : {Score}')
            again_Game()
            break
        if choice_player2 is not ['1','2']:
            print('invalid input',0)    


# start game      
def start_game():
    global Score
    # senario of adventure game
    sleep_print('You venture into the forest, following the directions on the signpost.') 
    sleep_print('\n As you walk deeper into the woods, the trees grow taller and the underbrush thickens') 
    sleep_print('\n The sunlight filtering through the leaves overhead casts dappled shadows on the ground. ')  
    sleep_print('\n You soon come across a fork in the path.')
    sleep_print('\n Now, you have two paths :')
    sleep_print('\n 1-Take the right path'+'\n'+'\n 2-Take the lift path\n')
    
    while True:
        choice_player=input('What would you like to do? Enter your choice 1 or 2?')# ask player to choose his path
        if choice_player=='1':# take the right path
            Score+=5# points
            right_path()
            break
        elif choice_player=='2':# take the left path
            Score+=10# points
            left_path()
            break
        elif choice_player is not ['1','2']:
            print('invalid choice',0)
def rules_game():# game rules if the player wants to know game rules before starting game
    sleep_print('Would you like to know rules of  game before you start playing? ') 
    gammer=input('Enter your choice :( yes or no): ').lower()
    if gammer=='yes':
        sleep_print('\n1-Each choice you make affects the outcome of the game and your score.'+'\n'+'\n2-The goal is to make choices that lead you to victory.')   
        sleep_print('\n3-Some choices may lead to failure or a game over, and you will need to restart the game.'+'\n'+'\n4-Your score will be shown at the end of the game based on the choices you made.')
        sleep_print('\n5-You cannot change your choices once you have made them.'+'\n'+'\n6-The game is just for fun, and isnot meant to be taken too seriously.')
        sleep_print('\nStart Adventure Game\n')
        start_game()
    elif gammer=='no':
        print('\nStart Adventure Game\n')
        start_game()    
    elif gammer is not ['yes','no']:
        print('invalid choice')
        return rules_game()
# to start game         
rules_game()    
print(f'Total Score: {Score}')