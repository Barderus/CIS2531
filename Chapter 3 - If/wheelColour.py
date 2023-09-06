'''
Author: Gabriel dos Reis
Date: 9/5/2023
Program: wheelColours.py
Description:Write a program that asks the user to enter a pocket number and displays 
whether the pocket is green, red, or black. 
The program should display an error message if the user enters a number that is outside 
the range of 0 through 36.

    *Pocket 0 is green.
    * Pockets 1 through 10
        the odd-numbered pockets are red and the even-numbered pockets are black.
    * Pockets 11 through 18
        the odd-numbered pockets are black and the even-numbered pockets are red.
    * Pockets 19 through 28
        the odd-numbered pockets are red and the even-numbered pockets are black.
    * Pockets 29 through 36
        the odd-numbered pockets are black and the even-numbered pockets are red.
'''

userChoice = int(input("Enter a pocket number: "))

# Identifying the colour of the pocket
# 0 is always green
if userChoice == 0:
    print("Pocket is Green!")   
elif userChoice >= 1 and userChoice <= 10: # Range 1 through 10 
    if userChoice % 2 == 1: # Odd numbers = red and even numbers = black
        print("Pocket is Red!")
    else:
        print("Pocket is Black!")
elif userChoice >= 11 and userChoice <= 18: #Range 11 through 18
    if userChoice % 2 == 1: #Odd numbers = black and even numbers = red
        print("Pocket is Black!")
    else:
        print("Pocket is Red!")   
elif userChoice >= 19 and userChoice <= 28: #Range 19 through 28
    if userChoice % 2 == 1: # Odd numbers = red and even numbers = black
        print("Pocket is Red!")
    else:
        print("Pocket is Black!")
elif userChoice >= 29 and userChoice <= 36: #Range 29 through 36
    if userChoice % 2 == 0: #Odd numbers = black and even numbers = red
        print("Pocket is Red!")
    else:
        print("Pocket is Black!")
else:
    print("Error! Invalid number! It must be between 0 and 36!")

'''
*** OUTPUT1: ***

Enter a pocket number: 12
Pocket is Black!

*** Ouput2: ***

Enter a pocket number: 41
Error! Invalid number! It must be between 0 and 36!
'''