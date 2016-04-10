#Assignment 1a Part1 - Roger Gilbertson - 28.03.16

# Savings calculator


# Functions
def calculateSavingsTotal(savingsPerWeek, numWeeks):                               #total savings function
    savings = savingsPerWeek * numWeeks                                            #total savings calculation
    return savings                                                                 #returning of value

def intInput(string):                                                              #int input function
    return int(input(string))

def main():
    savingsPerWeek = intInput('Please enter in amount saved per week : ')          #variable for savings per week
    numWeeks       = intInput('Please enter number of weeks : ')                   #variable for number of weeks
    savings        = calculateSavingsTotal(savingsPerWeek, numWeeks)               #savings calculation
    print("You can save a total of ${} over {} weeks.".format(savings, numWeeks))  #printing string in correct format

#code
main()                                                                             #call of main function