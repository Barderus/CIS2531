'''
Author: Gabriel dos Reis
Class: CIS2531 -- Intro to Python
Prog: CalcChnage.py
Date: 8/28/2023
Description: Calculate the least number of quarters, dimes, nickels
and pennies for a given amount of change. Less than a dollar 
'''

#Python named constants --> All upercase names
QUARTER = 25
DIME = 10
NICKEL = 5

# get input amount of change
inputChange = int(input("Enter the amount of change (whole number less than 100): "))

# Calculate change amount for each coin type
numQuarters = inputChange // QUARTER
change = inputChange - (numQuarters * QUARTER)
numDimes = change // DIME
change = change - (numDimes * DIME)
numNickel = change // NICKEL
numPennies = change - (numNickel * NICKEL)

#Print amount
print("For the change amount of", inputChange, " You will need:", \
    "\n\tQuarters =", numQuarters, "\n\tDimes =", numDimes, \
        "\n\tNickels =", numNickel, "\n\tPennies =", numPennies) 

