'''
Author: Gabriel dos Reis
Date: 9/13/2023
Program: countingLoop.py
Description: This program prompts the user for a number an it counts up to that number from 0.
'''
number = int(input("Enter a number: "))
x = 1
while x < (number+1):
    print(x, "little sheep")
    x += 1
print("It's bedtime!")