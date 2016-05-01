#Assignment 1B Part 3 - Roger Gilbertson - Student ID: 14292284 - 20.04.16

import random


def randomDescriptionGenerator():
    description        = ['Brand new', 'New Family', 'Dream', 'First']
    adjective          = ['Spacious', 'Modern', 'Wonderful', 'Sunny']
    bedroom            = ['one', 'two', 'three', 'four', 'five']
    suburb             = ['Takapuna', 'Milford', 'Devonport', 'Beach Haven', 'Auckland Central']
    type_of_owner      = ['a couple', 'a family', 'a retired couple', 'a large family', 'a professional couple']
    amenities_close_by = ['great schools', 'shopping centre', 'motorway', 'airport', 'hospital']
    values = dict(description='', adjective='', bedroom='', suburb='', type_of_owner='', amenities_close_by='')
    values.update(description=random.choice(description))
    values.update(adjective=random.choice(adjective))
    values.update(bedroom=random.choice(bedroom))
    values.update(suburb=random.choice(suburb))
    values.update(type_of_owner=random.choice(type_of_owner))
    values.update(amenities_close_by=random.choice(amenities_close_by))
    #print(values)
    return values


def printAdvertisement(formatedAdvertisement, values):
    # findValueField(formatedAdvertisement)
    formatedAdvertisement       = formatedAdvertisement.format(**values)                                                      #injects/replaces values from user input
    print(formatedAdvertisement)


# def findValueField(field):
#     valueFields   = list()
#     start       = field.find('<')
#     end         = field.find('>')
#     field       = field[start: end]
#     valueFields.append(field)
#     return set(valueFields)


def main():
    formatedAdventisement = '''
                     *** Your <description> Home ***
               <adjective> <bedrooms> bedroom home in <suburb>
                        Would suit <type of owner>
                    Close to <amenities_close_by>.
                All enquires to Joe Bloggs on 007 1234
                      *** Make it yours today! ***
                      '''
    values = randomDescriptionGenerator()
    printAdvertisement(formatedAdventisement, values)

main()