
#assignment 2a Question 2 Roger Gilbertson
import random

def load():
    movies_list = []
    fileName    = input("Please enter name of file (Default is 'movies.txt') :") or "movies.txt"

    try:                                                        #TRYS FUNCTION IF NOT MOVES TO EXCEPT
        print("Call of load")

        file = open(fileName, "r")                              # OPENS FILE
        movies_list = file.readlines()                          # LOADS EACH LINE INTO LIST
        movies_list = [movie.strip() for movie in movies_list]
        file.close()                                            # CLOSES FILE

        print(movies_list)

    except FileNotFoundError:                                   #IF FILE NOT FOUND DISPLAYS ERROR MESSAGE
        print('File could not be opened. Please check movies.txt is in same directory as .py file.\n \
               Returning to main menu.')

    return movies_list;


def randomSelection(movies_list):
    print('Random Movie Selection')

    matching_movies_list = [];
    matching_movies_list.append(random.choice(movies_list))
    print(matching_movies_list[0])
    return matching_movies_list;


def search(movies_list):
    print('Search of movies: ')

    matching_movies_list = []
    search_input         = [input('Enter word/s here to search: ')]

    for string in search_input:
        for item in movies_list:
            if string.lower() in item.lower():
                matching_movies_list.append(item)
                print(item, 'found')

    return matching_movies_list


def startsWith(movies_list):
    print('Search movies by start of name: ')

    matching_movies_list = []
    words_input          = [input('Enter word/s here to search: ')]

    for string in words_input:
        for item in movies_list:
            if item.lower().startswith(string.lower()):
                matching_movies_list.append(item)
                print(item)

    return matching_movies_list


def keep(favourites_list, last_movies_list):
    print('Keeping movie in Favourites')
    new_favourites_list = favourites_list + last_movies_list
    print(new_favourites_list);
    return new_favourites_list


def displayFavourites(favourites_list):
    print('Printing Favourites List')
    print(favourites_list)


def clearFavourites(favourites_list):
    print('Cleared Favourites')
    return []


def main():

    movies_list      = []
    last_movies_list = []
    favourites_list  = []
    quit             = False

    while quit == False:

        print("""
        *** Movie Title Explorer ***
            l – load file of movie titles
            r – random movie
            s – search
            sw – starts with
            k – keep - save the last displayed movie title to your favourites
            f – favourites display
            c – clear favourites
            q – quit
        command: ?""")

        userinput = input()

        if userinput == 'l':
            movies_list = load()

        elif userinput == 'q':
            quit = True;

        elif len(movies_list) == 0:                             #USES IF LENGTH OF 'MOVIE LIST' EMPTY  PRINT ERROR MESSAGE
            print('You need to load your movies file first!')

        elif userinput == 'r':
            last_movies_list = randomSelection(movies_list)

        elif userinput == 's':
            last_movies_list = search(movies_list)

        elif userinput == 'sw':
            last_movies_list = startsWith(movies_list)

        elif userinput == 'k':
            favourites_list = keep(favourites_list, last_movies_list)

        elif userinput == 'f':
            displayFavourites(favourites_list)

        elif userinput == 'c':
            favourites_list = clearFavourites(favourites_list)

    print('main end')

main()