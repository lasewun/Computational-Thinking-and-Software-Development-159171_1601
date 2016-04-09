#Assignment 1a Part1 - Roger Gilbertson - 28.03.16

# Savings calculator


# Functions
def calculateSavingsTotal(savingsPerWeek, numWeeks):                               #total savings function
    savings = savingsPerWeek * numWeeks                                            #total savings calculation
    return savings                                                                 #returning of value

# Variables
savingsPerWeek = int(input('Please enter in amount saved per week : '))            # variable for savings per week
numWeeks       = int(input('Please enter number of weeks : '))                     # variable for number of weeks

print("You can save a total of ${} over {} weeks".format(calculateSavingsTotal(savingsPerWeek, numWeeks), numWeeks))  #printing string in correct format
