# Assignment 1a Part 3 - Roger Gilbertson - 9.04.16

#Variables
def intro():                                                                                       #Intro
    print('     Weclome to Mad libs!')
    print('     Please provide the following to help')
    print('     create a new story')

def userInputValues():                                                                             #funcation for dictionarty of userinputs
    inputValues = dict(username=0, plural_noun=0, integer_value=0, body_part=0, verb=0)            #list of values to have values updated by user
    inputValues.update(username     =(str(input('Please enter name: '))))                          #update of value with user input
    inputValues.update(plural_noun  =(str(input('Please enter plural noun: '))))
    inputValues.update(integer_value=(str(input('Please enter integer value: '))))
    inputValues.update(body_part    =(str(input('Please enter body part: '))))
    inputValues.update(verb         =(str(input('Please enter verb: '))))
    return inputValues

def findValueField(value):                                                                         #function that scans 'story' for values to be replaced
    entryList   = list()                                                                           #start of list-empty
    start       = value.find('{')                                                                  #scans for '{' which is pointer to value to be replaced
    end         = value.find('}')                                                                  #scans for '}' which is end of pointer to value to be replaced
    entires     = value[start: end]                                                                #specifies that value in pointers gets replaced
    entryList.append(entires)                                                                      #appends value
    return set(entryList)                                                                          #returns list - updated

def printStory(printedStory):                                                                      #function that prints story with userinput values
    findValueField(printedStory)                                                                   #calls findValueField function
    inputValues = userInputValues()                                                                #calls userInputValues
    story       = printedStory.format(**inputValues)                                               #injects/replaces values from user input
    print(story)                                                                                   #prints story

def main():                                                                                        #main function
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
    printStory(story)                                                                              #calls printStory function using story
    return

#code
main()                                                                                             #call of main function