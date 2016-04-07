#Tutorial 3 Part 2a - Roger Gilbertson 26.03.16

#GST Calculator

#Variables
rate = 0
taxRates = (5, 10, 15, 20, 25)
usercost = input('Please enter cost of item : ')
itemName = input('Please enter name of item : ')

def taxCalc():                                          #calculator function
    global rate                                         #global or it doesnt work due to scope, need better way
    global GST
    GST = int(rate) * float(usercost)/100               #calculation
    rate = rate + 5                                     #value +5 for next time called
    return GST, rate                                    #saving global values for next call

def Calculation():                                      #Function that calls taxCalc
    for x in taxRates:                                  #for loop function to call taxCalc x5
        if x <= 25:
            taxCalc()
            print("{}% tax on a {} costing ${} is ${}".format(x, itemName, usercost,  format(GST, '.2f')))  #printing string in correct format



        else:                                           #not needed
            return




#Code  Calling of functions
taxCalc()
Calculation()

