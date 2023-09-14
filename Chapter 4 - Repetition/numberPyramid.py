'''
Author: Gabriel dos Reis
Date: 9/13/2023
Program: numberPyramid.py
Description: Create a program that generates a number of pyramid like the following:
1
12
123
1234
'''
# Prompt user for the pyramid size
rows = int(input("How many rolls would you like?: "))

for r in range(0, rows): # Each iteration forms a row
    for c in range(0, r + 1): # Each iteration forms a colum
        print(c+1," ", end="") 
    print()