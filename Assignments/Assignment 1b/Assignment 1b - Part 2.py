#Assignment 1B Part 2 - Roger Gilbertson - Student ID: 14292284 - 20.04.16

def multiples():
    num   = input('Multiples of: ')
    limit = input('Enter a upper limit: ')
    list  = []
    for num in range(int(num), int(limit)+1, int(num)):
        list.append(num)
    print(list)
    return list

def productCalc(list):
    product = 1
    for x in list:
        product *= x
    print('The product of the', list, 'is:', product)

def main():
    list = multiples()
    productCalc(list)

main()