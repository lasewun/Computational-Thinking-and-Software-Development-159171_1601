#Tutorial 6 Part 2 - Roger Gilbertson - Student ID: 14292284 - 29.04.16

# Money Dispenser Calculator


def dispenser(value):
    myList = [100, 50, 20, 1]                           #list of notes/coin to go through
    for item in myList:                                 #for loop for value of each item
        count = value // item
        value = value %  item

        if count > 0:                                   #if statement so only used notes/coin are printed (no 0 x $50 etc)
            print(item, 'x $' + str(count))


def main():
    value = int(input('Enter initial value here (int) :'))  #int input for dispenser function to use
    dispenser(value)

main()