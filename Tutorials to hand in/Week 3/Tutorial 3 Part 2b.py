#Tutorial 3 Part 2b - Roger Gilbertson 26.03.16

#note: only part coded by me was pickACard()
#coded out code was not overly complicated as there are only two variables
#used line for string formatting as this is what we recently studied

import random                                                                                   #import of random

#variables
suites = ["Hearts", "Diamonds", "Spades", "Clubs"]
cardFaces = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
cardFace = random.choice( cardFaces )                                                           #seemily useless variable. Not sure if I was expected to use this?

def pickACard():                                                                                #Function that creates card choice
    #return (str(random.choice(cardFaces)) + " of " + str(random.choice(suites)))               #coded out code. easiest way is the best but im sure you want me to show string formatting instead
    return ("{:s} of {:s}".format(str(random.choice(cardFaces)), str(random.choice(suites))))   #formating version of code as i believe this is what you're looking for.


hand =[]                                                                                        #list of cards



for i in range(5):                                                                              #loop
    card = pickACard()
    hand.append(card)



print(hand)                                                                                     #call of code