'''
Author: Gabriel dos Reis
Date: 9/13/2023
Program: nestedLoop.py
Description: Practicing more nested loops'''

rows = 5

for r in range(rows, 0, -1): # Starting from 5 to 0, step down 1
    for c in range(0, r): # For each colum it increases the row
        print(c+1, " ", end="")
    print()