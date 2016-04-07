#Exercise 2A - Roger Gilbertson 15.03.16

#values
num1 = float(input('enter first value : '))
num2 = float(input('enter second value : '))
num3 = float(input('enter third value : '))
TotalAmount = (num1 + num2 + num3)
def TotalGST(num1 , num2 , num3):
    return ((num1 + num2 + num3)*0.15)
#TotalGST = (float(TotalAmount) * 15 / 100)

#code
print('Total sum is ' + str(TotalAmount), "and the GST is " + str(TotalGST))

#note to self: Sweet it works, remember to convert/def in final line as str
#def TotalGST()a,b,c):
#return (a+b+c)*0.15

#print('the total gst is' TotalGST(value1,value2,value3))