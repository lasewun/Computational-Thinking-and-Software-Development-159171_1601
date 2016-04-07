#exercise p1i

#Total = 0
#for i in range(1,11):
#	print(i, '\t', (i)**3)
#	Total += (i) ** 3
#	Total = Total

#print ('total: ' ,Total)
#total is wrong check this




#exercise p1ii


#Total = 0
#for i in range(0,101,10):
#	print(i, '\t', (i)**3)
#	Total += (i) ** 3
#	Total = Total + i**3
#
#print ('total: ' ,Total)



#exercise bi

#sentence = input('enter sentence')
#list = sentence.split()
#print(list)

#for r in list:
#    print(r.upper(), '\t')


#a = input('how do you want to split sentence?')
#list.sentence.split(a)


#new
#exercise bi

#sentence = input('enter sentence : ')
#a = input('how do you want to split sentence?')
#list = sentence.split(a)
#print(list)



#exercise bii


#sentence = input('enter sentence : ')
#a = input('how do you want to split sentence?')
#list = sentence.split(a)
#print(list)

#for r in list:
#    print(r.upper(), '\n')

#for r in list:
#    print(r.title(), '\n')

#for r in list:
#    print(r.swapcase(), '\n')

#part 2 only for tutorial hand in

# print('Random letter guess')
# import random as rand
# ListLetter = ['a','b','c','d','e']
# target = rand.choice(ListLetter)
# found = False
# while not found:
#     guess = str(input("what's your guess?"))
#     if guess == target:
#         print("Good guess - you found it")
#         found = True
#
#     else:
#         if guess < target:
#             print('too low')
#         else:
#             print("too high")





###############part 3


import turtle #import the turtle module
for r in range(1,100):
    wn = turtle.Screen() # creates a graphics window
    my_turtle = turtle.Turtle() # create a turtle named my_turtle
    my_turtle.left(5**r)
    my_turtle.forward( 90)#go forward by amount my_turtle.left(90) # turn left by 90 degrees
    wn.exitonclick() # wait for a user click on the canvas
