#Tutorial 5 Part 2A - Roger Gilbertson - Student ID: 14292284 - 22.04.16


def printTable(copies, limit):
    for c in range(copies):
        for l in range(limit):
            print(l+1, end=" ")
        print()


def printRow(start_value, limit2):
    for value in range(start_value, limit2+1):
        print(value, end="\t")


def printNumberBlock(startVal, limitVal, numCopies):
    for c in range(numCopies):
        printRow(startVal, limitVal)
        print()


def main():
    limit = int(input('Please enter in limit : '))
    copies = int(input('Number of copies : '))
    printTable(copies, limit)                        #function to call printTable using input variables above
    limit2 = int(input('Please enter in limit : '))  #used limit2 instead of overwriting variable limit
    start_value = int(input("Enter in start value"))
    printRow(start_value, limit2)                    #function to call printRow using input variables above
    startVal = int(input('Please enter in start value : '))
    limitVal = int(input('Please enter in limit : '))
    numCopies = int(input('Please enter in number of copies : '))
    printNumberBlock(startVal, limitVal, numCopies)  #function to call printNumberBLock that has printTable using input variables above


main()