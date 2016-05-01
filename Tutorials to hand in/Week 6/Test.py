def main():
    purchamt, payamt = inputdata()
    change, dollars, quarters, dimes, nickels, pennies = calcchange(purchamt, payamt)
    printresults (change, dollars, quarters, dimes, nickels, pennies)
    return
# ========================================= input data
def inputdata():
    purchamt=float(input("Enter the cost of the item purchased: "))
    payamt=float(input("Enter the amount paid for the item: "))
    return purchamt, payamt
# ========================================= calculate the change
def calcchange(purchamt, payamt):
    change = payamt - purchamt
    cents = change*100+0.01
    print(cents)
    dollars = int(cents /100)
    cents = cents %100
    quarters = int(cents/25)
    cents = cents %25
    dimes = int(cents/10)
    cents = cents %10
    nickels = int(cents/5)
    cents = cents %5
    pennies = int(cents)
    return change, dollars, quarters, dimes, nickels, pennies
# ========================================= print results
def printresults(change, dollars, quarters, dimes, nickels, pennies):
    print
    print("Amount of change to give back: ", change)
    print('dollars: $', dollars)
    print('quarters: ', quarters)
    print('dimes: ', dimes)
    print('nickels: ', nickels)
    print('pennies: ', pennies)
    return
# ===================================== call the main
main()