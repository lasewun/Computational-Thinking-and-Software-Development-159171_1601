#Exercise B. - Roger Gilbertson 17.03.16

#Function
def avg4():                                                                         #defining/function name
    num1 = float(input('enter first value : '))                                     #input of user numbers
    num2 = float(input('enter second value : '))
    num3 = float(input('enter third value : '))
    num4 = float(input('enter fourth value : '))
    sum = (num1+num2+num3+num4)                                                     #adding of numbers together
    avg4 = (sum)/4                                                                  #sum divided by number of inputs(4)
    return avg4                                                                     #saving of value

#code
print('The average of these four numbers is :',(str(avg4())))                       #Print to check that value was saved




