# #exercise bi
#
# sentence = input('enter sentence : ')
# a = input('how do you want to split sentence?')
# list = sentence.split(a)
# print(list)
#
# for r in list:
#     print(r.upper(), '\t')


# ------------------------------------------------------------
#Student: Austin Wells
#Class: CS122
#Date: 4/2/2015
#Program Title: Programming Excercise 4.py
#Program Description: This program promts a user for five
#purchased items prices and returns a subtotal, amount of sales
#tax and the total.
# ------------------------------------------------------------

# SALES_TAX_CONST=0.06 #Formatted like an actual constant since python doesnt have actual constants
#
# NUMBER_OF_ITEMS=5
#
# # applies sales tax to the subtotal and returns the amount of sales tax
# def applySalesTax(totalPurchasePrice):
#
# 	salesTax = totalPurchasePrice * SALES_TAX_CONST
#
# 	return salesTax
#
# # prompts user for the price of five items and adds them into a list. It then returns the list
# def promtForItemPrice(strPromt):
#
#     itemList = []
#
#     for loop in range(0,NUMBER_OF_ITEMS):
#
#     	itemList.insert(loop, input(strPromt + str(loop + 1)+": "))
#         print('${:0,.2f} \n'.format(itemList[loop]))
#
#     return itemList
#
# # inputs the item list and calculates their total and returns the total
# def subTotal(passedItemList):
#
#     subTotalVar = 0
#
#     for num in range(0,NUMBER_OF_ITEMS):
#
#     	subTotalVar += passedItemList[num]
#
#     return subTotalVar
#
# # main driver calls the above functions and calculates the sales total
# def checkOut():
#
# 	subTotalVal = subTotal(promtForItemPrice("Please enter the price for the item "))
#
# 	salesTax = applySalesTax(subTotalVal)
#
# 	salesPrice = salesTax + subTotalVal
#
# 	saleTotals = subTotalVal, salesTax, salesPrice
#
# 	return saleTotals
#
# #prints out sale totals. Inputs saleTotals tuple from checkOut
# def printOut(saleTotals):
#
# 	recieptList=[saleTotals[0], saleTotals[1], saleTotals[2]]
#
# 	titleList=["Subtotal: ", "Sales Tax: ", "Total Cost: "]
#
# 	for title, value in zip(titleList, recieptList):
#
# 		print  '{} ${:0,.2f} \n' .format(title, value)
#
# printOut(checkOut())


print("NOTICE: All tips are rounded up or down to make payment easier with single bills")
print("NOTICE: I take no responsibility for this script overestimating a tip")

# As the other comment mentioned, this will crash for non-numberic input
cost = float(input("Cost of Meal: $")) # You can just put the $ in the string

# You were reusing a lot of code, instead you could create a tuple with all
# the percentage values and iterate through it one by one.
percents = (5, 10, 15, 20, 25)
for percent in percents:
    # for every different percentage in percents, print out the string and calculate the tip
    print("{}% of ${} is ${}".format(percent, cost, (cost * percent) / 100))

# Now if you want to edit/add any of the desired outputs you can just add the percentage to percents