#assignment 2a Question 3 Roger Gilbertson
def selectAll(stories):
    return stories;
 
 
def selectStroiesByAuthor(stories):
    storyResults = []
    author       = input('(displayStroiesByAuthor) Enter Author: ').lower()

    for story in stories:
        if story[1].lower() == author:
            storyResults.append(story)

    return storyResults

def selectStroiesByAuthorAndPattern(stories):
    storyResults   = []
    authorStories  = selectStroiesByAuthor(stories)
    patternStories = selectStroiesByPattern(stories)

    for authorStory in authorStories:
        for patternStory in patternStories:
            if authorStory[0] == patternStory[0] and authorStory[1] == patternStory[1]:
                storyResults.append(authorStory)

    return storyResults

def selectStroiesByPattern(stories):
    storyResults = []
    pattern      = input('(displayStroiesByPattern) Enter Pattern: ').lower()

    for story in stories:
        if pattern in story[0].lower():
            storyResults.append(story)

    return storyResults

def selectStoriesByWordCount(stories):
    storyResults = []
    wordCount    = int(input('(displayStoriesByWordCount) Enter Word Count: '))

    for story in stories:
        if len(story[0].split(' ')) < wordCount:
            storyResults.append(story)

    return storyResults


def main():
    stories = [
        ['With bloody hands, I say good-bye.', 'Frank Miller'],
        ['TIME MACHINE REACHES FUTURE!!! ... nobody there ...', 'Harry Harrison'],
        ['The baby\'s blood type? Human, mostly.', 'Orson Scott Card'],
        ['For sale: baby shoes, never worn.', 'Ernest Hemingway'],
        ['Corpse parts missing. Doctor buys yacht.', 'Margaret Atwood'],
        ['We kissed. She melted. Mop please!', 'James Patrick Kelly'],
        ['Starlet sex scandal. Giant squid involved.', 'Margaret Atwood'],
        ['Will this do (lazy writer asked)?', 'Ken McLeod'],
        ["I'm sorry, but there's not enough air in here for everyone. I’ll tell them you were a hero.",
         'J. Matthew Zoss'],
        [
            'Waking Up To Silence: Deafening silence. I strain my ears, praying there might be someone else still alive. The only noise I hear are the voices in my head',
            'Mike Jackson'],
        [
            "Not In My Job Description: Make sure it's done by the end of the day Jones.\nBut, sir, it's not in my ....\nJust do it, and remember, no blood.",
            'Mike Jackson'],
        [
            'Empty Baggage: The trunk arrived two days later. He lifted the lid and froze, it was empty. No arms, no legs, no head, nothing. Where was she?',
            'Mike Jackson'],
        [
            'Forgot My Own Name: The hospital said it was concussion.\nMight be permanent memory loss.\nCan\'t even remember my own name - which is handy considering who I am.',
            'Mike Jackson']
    ]
    quit = False

    while quit == False:

        selectedStories = []

        menu = """
             Stories Explorer
                all - displays all stories
                a   - finds story by author
                ap  - Find stories that are by a certain author and contain a certain word
                p   - Find stories that contain a certain pattern
                wc  - Find stories less than a certain number of words
                q   - quit
            command: ?"""

        print(menu)

        inputSelection = input()

        if inputSelection == 'all':
             selectedStories = selectAll(stories)

        elif inputSelection == 'a':
             selectedStories = selectStroiesByAuthor(stories)

        elif inputSelection == 'ap':
             selectedStories = selectStroiesByAuthorAndPattern(stories)

        elif inputSelection == 'p':
             selectedStories = selectStroiesByPattern(stories)

        elif inputSelection == 'wc':
            selectedStories = selectStoriesByWordCount(stories)

        elif inputSelection == 'q':
            quit = True
 
 
        for story in selectedStories:
            print('"' + story[0] + '"')
            print(' -- ' + story[1])
 
 
main()