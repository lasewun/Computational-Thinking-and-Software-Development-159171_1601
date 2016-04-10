# Assignment 1a Part 3 - Roger Gilbertson - 9.04.16

#Variables
def intro():                                                                                       #Intro
    print('     Welcome to Mad libs!')
    print('     Please provide the following to help')
    print('     create a new story')

def strInput(string):                                                                              #function for returning str input
    return str(input(string))

def userInputValues():                                                                             #functions for dictionary of userinputs
    inputValues = dict(username=0, plural_noun=0, integer_value=0, body_part=0, verb=0)            #list of values to have values updated by user
    inputValues.update(username     =strInput('Please enter a name: '))                            #update of value with user input
    inputValues.update(plural_noun  =strInput('Please enter a plural noun: '))
    inputValues.update(integer_value=strInput('Please enter an integer value: '))
    inputValues.update(body_part    =strInput('Please enter a body part: '))
    inputValues.update(verb         =strInput('Please enter a verb: '))
    return inputValues

def printStory(story, inputValues):                                                                #function that prints story with userinput values
    story       = story.format(**inputValues)                                                      #injects/replaces values from user input
    print(story)                                                                                   #prints story

def main():                                                                                        #main function
    inputValues = userInputValues()                                                                #calls userInputValues
    story = '''
        ----------------------------------------
        Here is your story
        The famous explorer {username} had nearly given up a life long quest to find
        the lost city of {plural_noun} when one day, the {plural_noun} found the explorer.
        Surrounded by {integer_value} {plural_noun} a tear came to {username}'s {body_part}.
        After all this time, the quest was finally over.
        And then, the {plural_noun} promptly devoured {username}.
        The moral of the story? Be careful what you {verb} for.
        ----------------The end-----------------
            '''
    intro()                                                                                        #call of intro function
    printStory(story, inputValues)                                                                 #calls printStory function using story

#code
main()                                                                                             #call of main function