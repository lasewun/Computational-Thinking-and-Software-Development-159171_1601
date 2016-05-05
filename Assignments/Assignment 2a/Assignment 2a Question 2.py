#assignment 2a Question 2
import random

movies_list = []
lastSelection = []
favouritesList = []


def load():
    try:
        print('Call of load')
        fileName = input("Please enter name of file (Default is 'movies.txt') :")
        file = open(fileName, "r")  # open the file
        movies_list = file.readlines()  # load each line into a list
        movies_list = [movie.strip() for movie in movies_list]
        file.close()  # close the file
        print(movies_list)
        return movies_list
    except FileNotFoundError:
        print('File could not be opened. Please check movies-2.text is in same directory as .py file.\n \
        Returning to main menu.')
        main(movies_list)


def randomSelection(movies_list):
    print('Call of random')
    try:
        lastSelection =(random.choice(movies_list))
        print(lastSelection)
        return lastSelection
    except IndexError:
        print('Choice could not be completed. Please check movies.txt or .txt file has been loaded first\n \
            Returning to main menu.')
        main()


def search(movies_list):
    print('Call of search')
    stringSearch = [input('Enter word/s here to search')]
    for string in stringSearch:
        for item in movies_list:
            if string in item:
                lastSelection = (item, 'found')
                print(lastSelection)
                return lastSelection


def startsWith(movies_list):
    print('Call of startswith')
    str = [input('Enter word/s here to search')]
    for string in str:
        for item in movies_list:
            if item.startswith(string):
                lastSelection = item
                print(lastSelection)
                return lastSelection


def keep(lastSelection):
    print('call of keep')
    favouritesList.append(lastSelection)


def favourites(favouritesList):
    print(favouritesList)
    return favouritesList


def clearFavourites(favouritesList):
    del favouritesList[:]
    print('Clearing')
    return favouritesList

def main(movies_list, lastSelection):
    movies_list
    lastSelection
    favouritesList
    menu = """
    *** Movie Title Explorer ***
        l – load file of movie titles
        r – random movie
        s – search
        sw – starts with
        k – keep - save the last displayed movie title to your favourites
        f – favourites display
        c – clear favourites
        q – quit
    command: ?"""

    print(menu)
    inputSelection = input('')
    while inputSelection != ('l', 'r', 's', 'sw', 'k', 'f', 'c'):

        if inputSelection == 'l':
            movies_list = load()
            main(movies_list, lastSelection)

        elif inputSelection == 'r':
            lastSelection = randomSelection(movies_list)
            main(movies_list, lastSelection)

        elif inputSelection == 's':
            search(movies_list)
            main(movies_list, lastSelection)

        elif inputSelection == 'sw':
            startsWith(movies_list)
            main(movies_list, lastSelection)

        elif inputSelection == 'k':
            keep(lastSelection)
            main(movies_list,lastSelection)

        elif inputSelection == 'f':
            favourites(favouritesList)
            main(movies_list, lastSelection)

        elif inputSelection == 'c':
            clearFavourites(favouritesList)
            main(movies_list, lastSelection)

        else:
            quit()
    else:
        print('ending')
        return
main(movies_list, lastSelection)