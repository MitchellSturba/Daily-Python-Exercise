#A game of Cows and Bulls
#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.”
import random


def GetCowsAndBulls(number, pGuess):
    #cowbulls[0] are the cows, cowbulls[1] are the bulls
    cowBulls = [0,0]
    for i in range(0,len(number)):
        #if number is correct than increment bulls, if wrong increment cows
        if number[i] == pGuess[i]:
            cowBulls[1] += 1
        else:
            cowBulls[0] += 1
    return cowBulls



if __name__ == "__main__":
    playing = True
    number = str(random.randint(0,9999))
    cowBulls = []
    playerGuesses = 0

    #welcome messages
    print('Welcome to the game of Cows and Bulls!')
    print('A four digit number has been generated and you have to guess the number')
    print('Every number wrong is a cow, and everyone correct is a bull')
    print('type exit to stop playing')

    while playing:
        pGuess = str(input('please enter a 4 digit number: '))

        if len(pGuess) != 4:
            continue

        #breaks game if user wishes to quit
        if pGuess == "exit":
            break

        #tests number
        cowBulls = GetCowsAndBulls(number, pGuess)

        #prints score so far
        print("Cows: " + str(cowBulls[0]) + " Bulls: " + str(cowBulls[1]))

        if (cowBulls[1] == 4):
            PA = input("CONGRATULATIONS YOU WIN!!\n The number was " + number + "\nPlay Again? (Yes, No)")
            if str.lower(PA) == "yes":
                number = str(random.randint(0,9999))
            else:
                print("Thanks for playing! ")
                quit()
                break
            

