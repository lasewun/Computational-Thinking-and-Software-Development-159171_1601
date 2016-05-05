# assignment 2a question 3



def displayAll(stories):
    stringSearch = [input('Enter word/s here to search')]
    for string in stringSearch:
        for item in stories:
            if string in item:
                print(item, 'found')
                return





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
    menu = """
    *** Stories Explorer ***
        all - displays all stories
        ath - finds story by author
        awd – Find stories that are by a certain author and contain a certain word
        lss – Find stories less than a certain number of words
        qit – quit
    command: ?"""
    print(menu)
    inputSelection = input('')
    while inputSelection != ('all', 'ath', 'awd', 'lss', 'qit'):
        if inputSelection == 'all':
            displayAll(stories)
            main()
main()


