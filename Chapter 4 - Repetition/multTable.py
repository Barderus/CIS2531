'''
Author: Gabriel dos Reis
Date: 9/13/2023
Program: multiplicationTable.py
Description: Write a program that asks the user for a number and then prints the multiplication
table for that number from 1 to 10 using a 'for' loop.
'''

# Prompt the user for a number
number = int(input("Enter a number: "))
for x in range(11):
    # Ex: 7 * x where x is each iteration of loop (1,2,3...etc)
    print(number * x)