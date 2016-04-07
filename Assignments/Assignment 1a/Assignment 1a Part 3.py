# Assignment 1a Part 3 - Roger Gilbertson - 7.04.16


#Variables
def intro():
    print('Weclome to Mad libs!')
    print('Please provide the following to help')
    print('create a new story')

def user_input(formatstring):
    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1 # pass the '{'
        end = formatString.find('}', start)
        key = formatString[start : end]
        keyList.append(key) # may add duplicates

    return set(keyList) # removes duplicates: no duplicates in a set







intro()


def getKeys(formatString):
    '''formatString is a format string with embedded dictionary keys.
    Return a set containing all the keys from the format string.'''

    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1 # pass the '{'
        end = formatString.find('}', start)
        key = formatString[start : end]
        keyList.append(key) # may add duplicates

    return set(keyList) # removes duplicates: no duplicates in a set

def addPick(cue, dictionary): # from madlibDict.py
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    promptFormat = "Enter a specific example for {name}: "
    prompt = promptFormat.format(name=cue)
    response = input(prompt)
    dictionary[cue] = response


def getUserPicks(cues):
    '''Loop through the collection of cue keys and get user choices.
    Return the resulting dictionary.
    '''
    userPicks = dict()
    for cue in cues:
        addPick(cue, userPicks)
    return userPicks

def tellStory(storyFormat):
    '''storyFormat is a string with Python dictionary references embedded,
    in the form {cue}.  Prompt the user for the mad lib substitutions
    and then print the resulting story with the substitutions.
    '''
    cues = getKeys(storyFormat)
    userPicks = getUserPicks(cues)
    story = storyFormat.format(**userPicks)
    print(story)

def main():
    originalStoryFormat = '''
Once upon a time, deep in an ancient jungle,
there lived a {animal}.  This {animal}
liked to eat {food}, but the jungle had
very little {food} to offer.  One day, an
explorer found the {animal} and discovered
it liked {food}.  The explorer took the
{animal} back to {city}, where it could
eat as much {food} as it wanted.  However,
the {animal} became homesick, so the
explorer brought it back to the jungle,
leaving a large supply of {food}.

The End
'''
    tellStory(originalStoryFormat)
    input("Press Enter to end the program.")


main()

# print('Here is your story'
#       'The famous explorer ',user_name,'had nearly given up a life long quest to find'
#       'the lost city of when one day, the cats found the explorer.'
#       'Surrounded by 'integer_value,plural_noun,'a tear came to ',user_name,"'s hair."
#       'After all this time, the quest was finally over'
#       'And then, the cats promptly devoured ',user_name,'.'
#       'The moral of the story? Be careful what you dream for.'
#       '----------------The end-----------------')