#Tutorial 3 Part 2a - Roger Gilbertson 26.03.16

#GST Calculator

#Variables
taxRates = [0.05, 0.10, 0.15, 0.20, 0.25]                   #tax rates from 5% -25% in 5% incredmints
itemCost = float(input('Please enter cost of item : '))     #user input of cost of item
itemName = input('Please enter name of item : ')            #user input of name of item

def calcuateItemTax(itemCost, taxRate):                     #calculator function
    taxAmount = taxRate * itemCost                          #calculation
    return taxAmount                                        #saving of value

def runCalculations():                                      #Function that calls calculateItemTax()
    for x in taxRates:                                      #for loop function to call function
        resultTaxAmount = calcuateItemTax(itemCost, x)
        print("{}% tax on a {} costing ${} is ${}".format(format(x* 100, '.0f'), itemName, itemCost, format(resultTaxAmount, '.2f')))  #printing string in correct format

#Code  Calling of function
runCalculations()