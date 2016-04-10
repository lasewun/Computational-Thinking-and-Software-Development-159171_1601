# Assignment 1a Part 3 - Roger Gilbertson - 9.04.16

#Variables
def intro():                                                                                       #Intro
    print('     Welcome to Mad libs!')
    print('     Please provide the following to help')
    print('     create a new story')

def userInputValues():                                                                             #funcation for dictionary of userinputs
    inputValues = dict(username=0, plural_noun=0, integer_value=0, body_part=0, verb=0)            #list of values to have values updated by user
    inputValues.update(username     =(str(input('Please enter a name: '))))                        #update of value with user input
    inputValues.update(plural_noun  =(str(input('Please enter a plural noun: '))))
    inputValues.update(integer_value=(str(input('Please enter an integer value: '))))
    inputValues.update(body_part    =(str(input('Please enter a body part: '))))
    inputValues.update(verb         =(str(input('Please enter a verb: '))))
    return inputValues

# def findValueField(value):                                                                         #function that scans 'story' for values to be replaced
#     entryList   = list()                                                                           #creates list - empty
#     start       = value.find('{')                                                                  #scans for '{' which is pointer to value to be replaced
#     end         = value.find('}')                                                                  #scans for '}' which is end of pointer to value to be replaced
#     entry       = value[start: end]                                                                #specifies that value in pointers gets replaced
#     entryList.append(entry)                                                                        #appends value
#     return set(entryList)                                                                          #returns list - updated

def printStory(story, inputValues):                                                                #function that prints story with userinput values
    #findValueField(story)                                                                          #calls findValueField function
    story       = story.format(**inputValues)                                                      #injects/replaces values from user input
    print(story)                                                                                   #prints story

def main():                                                                                        #main function
    inputValues = userInputValues()                                                                #calls userInputValues
    story = '''
        ----------------------------------------
        Here is your story lolol
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
    return

#code
main()                                                                                             #call of main function