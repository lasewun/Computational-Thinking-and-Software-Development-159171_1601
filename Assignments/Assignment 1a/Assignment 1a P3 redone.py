# Assignment 1a Part 3 - Roger Gilbertson - 7.04.16

#Variables
def intro():
    print('     Weclome to Mad libs!')
    print('     Please provide the following to help')
    print('     create a new story')
    return

def userInputValues():
    inputValues = dict()
    inputValues = dict(username=0, plural_noun=0, integer_value=0, body_part=0, verb=0)
    inputValues.update(username=(str(input('Please enter name: '))))
    inputValues.update(plural_noun=(str(input('Please enter plural noun: '))))
    inputValues.update(integer_value=(str(input('Please enter integer value: '))))
    inputValues.update(body_part=(str(input('Please enter body part: '))))
    inputValues.update(verb=(str(input('Please enter verb: '))))
    return inputValues

def findValueField(value):
    entryList   = list()
    start       = value.find('{')
    end         = value.find('}', start)
    entires     = value[start: end]
    entryList.append(entires)
    return set(entryList)

def printStory(storyFormat):
    findValueField(storyFormat)
    inputValues = userInputValues()
    story = storyFormat.format(**inputValues)
    print(story)

def main():
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
    intro()
    printStory(story)
    return

#code
main()