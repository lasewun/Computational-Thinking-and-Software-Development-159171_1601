#Assignment 1B - Roger Gilbertson

# Investment calculator
#
# Calc = S=P(1+(j/n))^nt
# S is the final value of investment
# P is the initial value of the investment
# j is th annual interest rate
# n is the number of times that interest in compounded per year
# t is the number of years that money is invested for

initialInvestmentValue    = input('Initial investment Value is : ')
annualInterestRate        = input('Annual interest rate is: '     )
numTimessInterestCompound = input('Number of times that interest in compounded per yer : ')
numYearsMoneyInvested     = input('Number of years invested : ')

for i in range(numYearsMoneyInvested):
    savings = savings * (1 + annualInterestRate)

print(savings)

# def main():
#     print("This program calculates the future value")
#     print("of a 10-year investment.")
#
#     principal = input("Enter the amount invested each year: ")
#     apr = input("Enter the annual interest rate: ")
#     years = input("Enter the number of years: ")
#
#     for i in range(1, int(years) +1 ):
#         principal = float(principal) * (1 + float(apr))
#         print("The value in", i, " years is:", principal)
#
#
# main()
import sys

# Python 2/3 compatibility shim
# if sys.hexversion < 0x3000000:
#     rng = xrange
#     inp = raw_input
# else:
#     rng = range
#     inp = input
#
# def getter_fn(datatype):
#     if datatype == str:
#         return inp
#     else:
#         def fn(prompt=''):
#             while True:
#                 try:
#                     return datatype(inp(prompt))
#                 except ValueError:
#                     pass
#         return fn
#
# get_float = getter_fn(float)
# get_int   = getter_fn(int)
#
# def main():
#     print("Welcome to Letmeretire.com's financial retirement calculator!")
#
#     principal  = get_float("Initial investment amount? ")
#     periods    = get_int  ("How many years will you make an annual deposit? ")
#     deposit    = get_float("Annual deposit amount? ")
#     apr        = get_float("Annual interest rate (in percent)? ") / 100
#     retirement = get_int  ("Years until retirement? ")
#
#     deposits    = [deposit] * periods
#     no_deposits = [0.] * (retirement - periods)
#
#     amount = principal
#     for yr, d in enumerate(deposits + no_deposits, 1):
#         amount = (amount + d) * (1. + apr)
#         print('After {:>2d} year{} you have:   $ {:>10.2f}'.format(yr, 's,' if yr > 1 else ', ', amount))
#
# main()