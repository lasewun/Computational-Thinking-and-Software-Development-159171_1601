# Tutorial 9 Part 2 - Roger Gilbertson

amount  = 0
balance = 0                                                         #intitial amount

def setBalance(amt):
    global balance
    balance = amt

def printBalance():
    print('The balance is ${:10.2f}'.format(balance))

def printLedgerLine(date, amount, details):   #check 40mins for formatting
    print('{:<20s}{:<20s}${:>8.2f}${:>8.2f}'.format(date, details, amount, balance))

def withdraw(date, details, amount):
    global balance
    balance -= amount
    printLedgerLine(date, amount, details)

def deposit(date, details, amount):
    global balance
    balance += amount
    printLedgerLine(date, amount, details)

setBalance(500)
printBalance()
withdraw("17-12-2012", "BP - petrol", 72.50)
withdraw("19-12-2012", "Countdown", 55.50)
withdraw("20-12-2012", "munchies", 1.99)
withdraw("22-12-2012", "Vodafone", 20)
deposit ("23-12-2012",  "Income", 225)
withdraw("24-12-2012", "Presents", 99.02)
printBalance()
