#Tutorial 4 - Part 2 - Exercise B - Roger Gilbertson - 16/04/16

def translate(word,language):                                                                           #translate function
    if word == 'cat':                                                                                   #if or else for 'word' selection for cat or dof
        if  language == 'German':                                                                       #nested if statements for languages selection
            translation = 'Katza'
        elif language == 'French':
            translation = 'Chat'
        elif language == 'Spanish':
            translation = 'Gato'
        else:
            translation = 'Incorrect language selection'
    elif word == 'dog':
        if  language == 'German':
            translation = 'Hund'
        elif language == 'French':
            translation = 'Chein'
        elif language == 'Spanish':
            translation = 'Perro'
        else:
            translation = 'Incorrect language selection'
    else:
        translation = 'Incorrect word selection'

    statement = "The translation of {} into {} is '{}'.".format(word, language, translation)            #statement printed with the selection of word and language followed by translation
    print(statement)

def userInput():                                                                                        #function that takes userinput and places them into an easy to use dictionary
    entries = dict(word="", language="")
    entries.update(word    =str(input("Enter in 'cat' or 'dog' to be translated : "                                 )))
    entries.update(language=str(input("Options: French, German, Spanish. \nEnter in language to be translated to : ")))
    return entries

def main():                                                                                             #main function that calls userInput and translate functions
    entries = userInput()
    translate(**entries)

main()


