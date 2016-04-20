#Tutorial 4 - Part 2 - Exercise A - Roger Gilbertson - 16/04/16 - 17/04/16

import random as rand                                                       # random function used for randomisation of name choice this is used with listNames to extend playability(also to limit choices of names player has)

def intro():
    print('Guess my name game. My name is either ' + str(listNames))        #intro displaying name choices

def userGuessInput():                                                       #userinput function that returns user input
    guessInput = str(input("What's your guess? "))
    return guessInput

def guessGame():                                                            #guessGame function that uses userguessinput.
    target = rand.choice(listNames)
    found = False
    while not found:                                                        #while function used to keep looping until name guessed
        guessInput = userGuessInput()
        guess = guessInput
        if guess.lower() == target.lower():                                 #converts string and name to lower case making capitilisation not an issue
            print('Got it!')
            found = True
        else:
            print('Guess again')

def main():                                                                 #main function calling userinput and gameguess functions
    intro()
    guessGame()

listNames = ['Steve', 'Andy', 'Charles', 'Roger', 'Sally']                  #list of names player has to guess from
main()