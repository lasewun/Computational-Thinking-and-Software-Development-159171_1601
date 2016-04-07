print('Random number guess')
import random as rand
target = rand.randint(1,100)
found = False
while not found:
    guess = int(input("what's your guess?"))
    if guess == target:
        print("Good guess - you found it")
        found = True
    else:
        if guess < target:
            print('too low')
        else:
            print("too high")



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