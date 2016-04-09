#Assignment 1a Part 2 - Roger Gilbertson - 28.03.16

#string length calculator

#variables
listOfStrings   = []                                                    #list of entries
numberOfEntries = (int(input('How many entries will there be? : ')))    #user specified length of list

def stringEntry(index):                                                      #Function returns user input
    return str(input('Please enter string '+str(index + 1)+' here : '))                   #code of function

def stringLength():                                                     #function that prints
    total = 0
    for string in listOfStrings:                                        #for loop to get string length user inputted number of times
        stringLength = len(string)
        print("The length of string ", string, "is ", str(stringLength))
        total += stringLength

    print("All strings total to length " + str(total))                  #prints sum of string lengths

#code

for i in range(numberOfEntries):                                        #for loop for user specified string length
    strings = stringEntry(i)
    listOfStrings.append(strings)

print(listOfStrings)
stringLength()


#Assignment 1a Part 2 - Roger Gilbertson - 28.03.16

#string length calculator

#variables
# listOfStrings = []                                                      #list of entries
# numberOfEntries = (int(input('How many entries will there be? : ')))    #user specified length of list
#
# def stringEntry():                                                      #Functions returns user input
#     return str(input('Please enter in word here : '))                      #code of function
#
# def stringLength():
#     total = 0
#     for string in listOfStrings:
#         stringLength = len(string)
#         print(string + " length is " + str(stringLength))
#         total += stringLength
#
#     print("All strings total to length " + str(total))
#
#     #return len(listOfStrings)
# #code
#
# for i in range(numberOfEntries):                                        #for loop for user specified string length                                               #loop
#     string = stringEntry()
#     listOfStrings.append(string)
#
# print(listOfStrings)
# stringLength()