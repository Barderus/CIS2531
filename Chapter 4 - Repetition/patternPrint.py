'''
Author: Gabriel dos Reis
Date: 9/13/2023
Program: patternPrint.py
Description: Write a program that prints * in each line increasing in each row
'''
number_star = int(input("How many rows would you like?: "))
for rows in range(0, number_star): # Iteration from 0 to whatever number the user entered
    for colums in range(0, rows + 1): #Iteration from 0 to rows +1
        print("*", end="")
    print()