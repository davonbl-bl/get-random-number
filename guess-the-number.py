import random;
import math;
import sys;

# getRandomNum = math.floor((random.random() * 50) + 1);
getEasyRandomNum = math.floor((random.random() * 50) + 1);
getMediumRandomNum = math.floor((random.random() * 50) + 1);
getHardRandomNum = math.floor((random.random() * 50) + 1);
# print(getRandomNum)

easyNumberOfChoices = 10; 
mediumNumberOfChoices = 5;
hardNumberOfChoices = 7; 

def playGame():
    playGames = input('Do you want to play this game? (yes/no)\n');
    if playGames.lower() == 'yes':
        stepsToTheGame();
    else:
        print('Okay. Have a nice day');
    
def stepsToTheGame():
    # getRandomNum = math.floor(random.random() * 50);
    # print('\nYou have to guess the correct number that is between 1 and 50. If you guess right, then you win the game!\n However, you can only guess five times. After guessing five times, you lose the game.\n')
    answer= input('Do you want to play this game in easy, medium, or hard difficulty?').lower()

    if (answer == 'easy'):
        print('\nYou have to guess the correct number that is between 1 and 50. If you guess right, then you win the game!\n However, you can only guess ten times. After guessing five times, you lose the game.\n')
        easyMode();
    elif(answer == 'medium'):
        print('\nYou have to guess the correct number that is between 1 and 50. If you guess right, then you win the game!\n However, you can only guess five times. After guessing five times, you lose the game.\n')
        mediumMode();
    elif(answer == 'hard'):
        print('\nYou have to guess the correct number that is between 1 and 200. If you guess right, then you win the game!\n However, you can only guess sevem times. After guessing five times, you lose the game.\n')
        hardMode()
    else:
        answer = input('Are you sure you want to leave? (yes/no)\n')
        if(answer == 'no'):
            stepsToTheGame()
        else:
            sys.exit()

def easyMode():
    global getEasyRandomNum;
    global easyNumberOfChoices; 

    yourNumber =int(input("What is the number?"));

    if(yourNumber == getEasyRandomNum):
        print('You win!')
        easyNumberOfChoices = 10
        # create an input asking if they want to play again, and this can be a seprate function 
        sys.exit()
    elif(yourNumber > getEasyRandomNum):
        print('the actual number is lower')
        easyNumberOfChoices= easyNumberOfChoices - 1
        print(easyNumberOfChoices)
        
    else:
        print('the actual number is higher')
        easyNumberOfChoices = easyNumberOfChoices - 1
        print(easyNumberOfChoices)

    if easyNumberOfChoices == 0:
        print('It\'s game over. Try next time.\n')
        print(f'The correct number was {getEasyRandomNum}')
        sys.exit()

    easyMode()


def mediumMode():
    global getMediumRandomNum;
    global mediumNumberOfChoices;

    yourNumber = int(input("What is the number?"));

    if(yourNumber == getMediumRandomNum):
        print('You win!')
        mediumNumberOfChoices = 5
        # create an input asking if they want to play again, and this can be a seprate function 
        sys.exit()
    elif(yourNumber > getMediumRandomNum):
        print('the actual number is lower')
        mediumNumberOfChoices= mediumNumberOfChoices - 1
        print(mediumNumberOfChoices)
        
    else:
        print('the actual number is higher')
        mediumNumberOfChoices = mediumNumberOfChoices - 1
        print(mediumNumberOfChoices)

    if mediumNumberOfChoices == 0:
        print('It\'s game over. Try next time.\n')
        print(f'The correct number was {getMediumRandomNum}')
        sys.exit()

    mediumMode()

def hardMode():
    global getHardRandomNum;
    global hardNumberOfChoices; 

    yourNumber = int(input("What is the number?"));

    if(yourNumber == getHardRandomNum):
        print('You win!')
        hardNumberOfChoices = 7
        # create an input asking if they want to play again, and this can be a seprate function 
        sys.exit()
    elif(yourNumber > getHardRandomNum):
        print('the actual number is lower')
        hardNumberOfChoices= hardNumberOfChoices - 1
        print(hardNumberOfChoices)
        
    else:
        print('the actual number is higher')
        hardNumberOfChoices = hardNumberOfChoices - 1
        print(hardNumberOfChoices)

    if hardNumberOfChoices == 0:
        print('It\'s game over. Try next time.\n')
        print(f'The correct number was {getHardRandomNum}')
        sys.exit()

    hardMode()

playGame()

# Just a basic function in the game, then deal with the add=ons later
