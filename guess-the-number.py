import random;
import math;
import sys;

getRandomNum = math.floor((random.random() * 50) + 1);
# print(getRandomNum)

numberOfChoices = 5;

def playGame():
    playGames = input('Do you want to play this game? (yes/no)\n');
    if playGames.lower() == 'yes':
        stepsToTheGame();
    else:
        print('Okay. Have a nice day');
    
def stepsToTheGame():
    # getRandomNum = math.floor(random.random() * 50);
    print('You have to guess the correct number that is between 1 and 50. If you guess right, then you win the game!\n However, you can only guess five times. After guessing five times, you lose the game.\n')
    guessTheNumGame();
    

def guessTheNumGame():
    # global getRandomNum;
    global numberOfChoices; 
    # guessThisNum = getRandomNum;
    yourNumber =int(input("What is the number?"));

    if(yourNumber == getRandomNum):
        print('You win!')
        numberOfChoices = 5
        # create an input asking if they want to play again, and this can be a seprate function 
        sys.exit()
    elif(yourNumber > getRandomNum):
        print('the actual number is lower')
        numberOfChoices= numberOfChoices - 1
        print(numberOfChoices)
        
    else:
        print('the actual number is higher')
        numberOfChoices = numberOfChoices - 1
        print(numberOfChoices)

    if numberOfChoices == 0:
        print('It\'s game over. Try next time.\n')
        print(f'The correct number was {getRandomNum}')
        sys.exit()

    guessTheNumGame()

playGame()

# Just a basic function in the game, then deal with the add=ons later
