'''
Author: Gabriel dos Reis
Date: 9/13/2023
Program: sumEvenNumbers.py
Description: Write a program that calculates and prints the sum of all even numbers
from 1 to 100 using a 'for' loop.
'''
user_number = int(input("Enter a number for a sum of even number: "))
even_number = 0
for x in range(user_number + 1):
    if x % 2 == 0:
        even_number += x
print(even_number)