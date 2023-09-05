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