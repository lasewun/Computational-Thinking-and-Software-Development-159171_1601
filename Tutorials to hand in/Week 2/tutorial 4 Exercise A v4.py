#Exercise A v4. - Roger Gilbertson 15.03.16 Ammended 17.03.16

#Function
def avg():                                                          #defining/function name
    num1 = float(input('enter first value : '))                     ##input of user numbers
    num2 = float(input('enter second value : '))
    num3 = float(input('enter third value : '))
    total = (num1 + num2 + num3)                                    #adding of numbers together
    mean = total/3                                                  #sum divided by number of inputs(3)
    print('The average of these three numbers is :'+(str(mean)))    #printing of text followed by value

#code
avg()                                                               #call of function
